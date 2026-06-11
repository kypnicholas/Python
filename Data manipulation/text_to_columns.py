import argparse
import pandas as pd
import glob
from pathlib import Path
import re
from io import StringIO


DEFAULT_INPUT_PATTERN = r'C:\Users\nkypri01\NK_DEV\1_Python\data_migration_VX\data\raw\*.csv'
DEFAULT_OUTPUT_DIR = r'C:\Users\nkypri01\NK_DEV\1_Python\data_migration_VX\data\processed'
DEFAULT_DELIM = ';'


def safe_read_csv(path: Path, encoding: str = 'utf-8-sig'):
    """Robust CSV reader with fallbacks and simple header heuristics."""
    last_exc = None

    # 1) try pandas default
    try:
        df = pd.read_csv(path, encoding=encoding)
        if df.shape[1] == 1:
            try:
                text = Path(path).read_text(encoding=encoding, errors='replace')
            except Exception:
                text = None
            if text and any(';' in ln for ln in text.splitlines()[:5]):
                return pd.read_csv(path, sep=';', engine='python', encoding=encoding)
        return df
    except Exception as e:
        last_exc = e

    # 2) try semicolon with python engine
    try:
        return pd.read_csv(path, sep=';', engine='python', encoding=encoding)
    except Exception as e:
        last_exc = e

    # 3) try to reconstruct from detected header line
    try:
        text = Path(path).read_text(encoding=encoding, errors='replace')
    except Exception as e:
        text = None
        last_exc = e

    if text:
        lines = text.splitlines()
        for idx, ln in enumerate(lines[:50]):
            if not ln or not ln.strip():
                continue
            s = ln.strip().lstrip('\ufeff')
            if re.match(r'^(sep|encoding)\s*=\s*', s, re.I):
                continue
            candidate = s.lstrip('#').lstrip()
            tokens_semi = [t for t in candidate.split(';') if t.strip()]
            tokens_comma = [t for t in candidate.split(',') if t.strip()]
            if len(tokens_semi) >= 2 and len(tokens_semi) >= len(tokens_comma):
                sep = ';'
            elif len(tokens_comma) >= 2:
                sep = ','
            else:
                continue
            remainder = [l for l in lines[idx+1:] if not l.lstrip().startswith('#')]
            reconstructed = '\n'.join([candidate] + remainder)
            try:
                return pd.read_csv(StringIO(reconstructed), sep=sep, engine='python')
            except Exception as e:
                last_exc = e

    print(f'Failed to parse {path}; last error: {last_exc}')
    if text:
        print('\n--- Diagnostic: first 40 lines (showing counts) ---')
        for i, ln in enumerate(text.splitlines()[:40], 1):
            print(f"{i:03d}: semi={ln.count(';')}, comma={ln.count(',')} | {ln!r}")
    raise last_exc if last_exc is not None else RuntimeError('Unknown CSV parse error')


def detect_candidate_column(df: pd.DataFrame, delim: str) -> str:
    """Return a column name that appears to contain the delimiter frequently, or None."""
    for col in df.columns:
        try:
            ser = df[col].dropna().astype(str)
            if ser.str.contains(re.escape(delim)).sum() > 0:
                return col
        except Exception:
            continue
    return None


def process_files(input_pattern: str, output_dir: str, column: str, delim: str, suffix: str, auto_detect: bool, preview: bool):
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    files = glob.glob(input_pattern)
    if not files:
        print('No files found for pattern:', input_pattern)
        return

    for file in files:
        p = Path(file)
        try:
            df = safe_read_csv(p)
        except Exception as e:
            print(f'Failed to read {p}: {e}')
            continue

        col_to_split = column
        if not col_to_split and auto_detect:
            col_to_split = detect_candidate_column(df, delim)
            if col_to_split:
                print(f'Auto-detected column `{col_to_split}` in {p.name}')

        if not col_to_split or col_to_split not in df.columns:
            print(f"Skipping {p.name}: '{column or '<auto>'}' column not found. Available columns: {list(df.columns)[:20]}")
            continue

        if preview:
            print(f'Preview: would split column `{col_to_split}` in {p.name} using delimiter "{delim}"')
            continue

        new_cols = df[col_to_split].astype(str).str.split(delim, expand=True)
        new_col_names = [f'{col_to_split}_part{i+1}' for i in range(new_cols.shape[1])]
        new_cols.columns = new_col_names
        df = pd.concat([df, new_cols], axis=1)

        out_name = f"{p.stem}{suffix}.csv"
        out_path = out_dir / out_name
        try:
            df.to_csv(out_path, index=False)
            print(f'Wrote processed file to {out_path}')
        except Exception as e:
            print(f'Failed to write {out_path}: {e}')


def main(argv=None):
    import argparse

    parser = argparse.ArgumentParser(description='Apply text-to-columns to multiple CSVs and save outputs to a separate folder')
    parser.add_argument('-i', '--input-pattern', default=DEFAULT_INPUT_PATTERN, help='Glob pattern for input CSVs')
    parser.add_argument('-o', '--output-dir', default=DEFAULT_OUTPUT_DIR, help='Directory to write processed files')
    parser.add_argument('-c', '--column', default=None, help='Source column to split (if omitted, use --auto-detect)')
    parser.add_argument('-d', '--delimiter', default=DEFAULT_DELIM, help='Delimiter to split the column by')
    parser.add_argument('-s', '--suffix', default='_processed', help='Suffix to append to output filenames')
    parser.add_argument('--auto-detect', action='store_true', help='Auto-detect a candidate column that contains the delimiter')
    parser.add_argument('--preview', action='store_true', help='Preview actions without writing files')
    args = parser.parse_args(argv)

    # If the user did not specify a column, enable auto-detection by default
    if args.column is None and not args.auto_detect:
        args.auto_detect = True

    process_files(args.input_pattern, args.output_dir, args.column, args.delimiter, args.suffix, args.auto_detect, args.preview)


if __name__ == '__main__':
    main()
