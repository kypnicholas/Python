"""CSV join/enrichment utility.

This script reads two CSV files, validates the join assumptions, and writes a new
CSV file with an additional column populated from a lookup table.

Typical use case
----------------
Enrich an order file with a parent/customer identifier before loading data into
Salesforce or another target system.

Example
-------
python enrich_csv_join.py `
    --source1 Customer.csv `
    --source2 Order.csv `
    --join "uid=User" `
    --copy-from customerID `
    --new-column Hybris_ID__c

Behavior
--------
- `--source1` is the lookup/source table.
- `--source2` is the file to enrich.
- `--join` is provided in the form "source1_column=source2_column".
- `--copy-from` is the column in source1 whose value should be copied.
- `--new-column` is the column created in source2.
- The output file name is automatically derived from `source2` by appending
    "_enriched" before the file extension (e.g. `Order.csv` -> `Order_enriched.csv`).

More CLI options
---------------
- `--write-samples`: when set, writes small CSV samples for failing checks
    (unmatched, duplicate, missing, ambiguous).
- `--sample-size N`: number of sample rows to capture/write for failures
    (default: 25).
- `--samples-dir DIR`: directory to write sample CSVs; defaults to the parent
    directory of `--source2`.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Tuple, Optional, Dict, Any

import pandas as pd


def parse_join_expression(join_expr: str) -> Tuple[str, str]:
    """Parse a join expression of the form "left_col=right_col".

    The left side refers to --source1 and the right side refers to --source2.
    """
    if "=" not in join_expr:
        raise ValueError('Join expression must be in the form "source1_column=source2_column".')

    left, right = join_expr.split("=", 1)
    left = left.strip()
    right = right.strip()

    if not left or not right:
        raise ValueError('Join expression must be in the form "source1_column=source2_column".')

    return left, right


def derive_output_path(source2_path: Path) -> Path:
    """Create the output file path by appending _enriched before the extension."""
    stem = source2_path.stem
    suffix = source2_path.suffix or ".csv"
    return source2_path.with_name(f"{stem}_enriched{suffix}")


def print_check(title: str, value: str) -> None:
    """Pretty console output for validation checks."""
    print(f"\n[{title}]\n{value}")


def validate_inputs(
    source1: pd.DataFrame,
    source2: pd.DataFrame,
    join_left: str,
    join_right: str,
    copy_from: str,
    sample_size: int = 25,
    return_samples: bool = False,
) -> Dict[str, Any]:
    """Run the requested checks before performing the enrichment.

    Checks covered:
    1. Join key coverage
    2. Uniqueness of the source key
    3. External ID / copy-from coverage
    4. Consistency of the join / ambiguity detection

    Returns:
        dict — structured results including counts, failing key lists and,
        optionally, sample DataFrames when `return_samples=True`.
    """
    # Confirm required columns exist.
    if join_left not in source1.columns:
        raise ValueError(f'Join column "{join_left}" was not found in source1.')
    if join_right not in source2.columns:
        raise ValueError(f'Join column "{join_right}" was not found in source2.')
    if copy_from not in source1.columns:
        raise ValueError(f'Copy-from column "{copy_from}" was not found in source1.')

    # Standardize join columns and copy column to string for comparison and reporting.
    s1 = source1.copy()
    s2 = source2.copy()
    s1[join_left] = s1[join_left].astype("string")
    s2[join_right] = s2[join_right].astype("string")
    s1[copy_from] = s1[copy_from].astype("string")

    # ---------------------------------------------------------------------
    # Check 1: Join key coverage
    # ---------------------------------------------------------------------
    source1_keys = s1[join_left].dropna()
    source2_keys = s2[join_right].dropna()

    matched_keys = source2_keys.isin(set(source1_keys))
    match_count = int(matched_keys.sum())
    total_source2_keys = int(source2_keys.shape[0])
    unmatched_count = total_source2_keys - match_count

    # Percentages for easier interpretation
    non_null_pct = (total_source2_keys / len(source2) * 100) if len(source2) > 0 else 0.0
    match_pct = (match_count / total_source2_keys * 100) if total_source2_keys > 0 else 0.0
    unmatched_pct = 100.0 - match_pct if total_source2_keys > 0 else 0.0

    coverage_msg = (
        f"source1 rows: {len(source1):,} | source2 rows: {len(source2):,}\n"
        f"source2 non-null join keys: {total_source2_keys:,} ({non_null_pct:.1f}% of source2)\n"
        f"matching source2 rows: {match_count:,} ({match_pct:.1f}%)\n"
        f"unmatched source2 rows: {unmatched_count:,} ({unmatched_pct:.1f}%)\n\n"
        "Action: Unmatched rows will produce empty values in the enrichment column."
    )
    print_check("CHECK 1 - JOIN KEY COVERAGE", coverage_msg)

    # Print the failing PK values for unmatched rows (join key values from source2)
    if unmatched_count > 0:
        try:
            unmatched_mask = s2[join_right].notna() & ~s2[join_right].isin(set(source1_keys))
            unmatched_keys = s2.loc[unmatched_mask, join_right].astype(str)
            unique_unmatched = list(dict.fromkeys(unmatched_keys.tolist()))  # preserve order, dedupe
            n_unmatched = len(unique_unmatched)
            max_show = 200
            shown = unique_unmatched[:max_show]
            more = n_unmatched - len(shown)
            keys_msg = f"Unmatched {join_right} values ({n_unmatched} total): {shown}"
            if more > 0:
                keys_msg += f" ... and {more} more"
            print_check("FAILED KEYS - UNMATCHED", keys_msg)
        except Exception:
            pass

    # ---------------------------------------------------------------------
    # Check 2: Uniqueness of the source key
    # ---------------------------------------------------------------------
    key_counts = source1_keys.value_counts(dropna=True)
    duplicate_keys = key_counts[key_counts > 1]
    duplicate_count = len(duplicate_keys)
    if duplicate_count == 0:
        uniqueness_msg = "No duplicate join keys found in source1."
    else:
        sample_duplicates = duplicate_keys.head(10).to_dict()
        uniqueness_msg = (
            f"Duplicate join keys in source1: {duplicate_count:,} keys\n"
            f"Sample (key:count): {sample_duplicates}\n\n"
            "Action: Enrichment will use the first occurrence for duplicate keys; consider deduping."
        )

    print_check("CHECK 2 - SOURCE KEY UNIQUENESS", uniqueness_msg)

    # Print duplicate join key values from source1 (the keys that are not unique)
    if duplicate_count > 0:
        try:
            dup_keys_list = [str(k) for k in duplicate_keys.index.tolist()]
            n_dup = len(dup_keys_list)
            max_show = 200
            shown = dup_keys_list[:max_show]
            more = n_dup - len(shown)
            dup_msg = f"Duplicate source1 join keys ({n_dup}): {shown}"
            if more > 0:
                dup_msg += f" ... and {more} more"
            print_check("FAILED KEYS - DUPLICATE_SOURCE1_KEYS", dup_msg)
        except Exception:
            pass

    # ---------------------------------------------------------------------
    # Check 3: Copy-from column coverage
    # ---------------------------------------------------------------------
    missing_value_count = int(s1[copy_from].isna().sum())
    empty_value_count = int((s1[copy_from].fillna("").str.strip() == "").sum())
    total_value_rows = len(s1)
    missing_pct = (missing_value_count / total_value_rows * 100) if total_value_rows > 0 else 0.0
    empty_pct = (empty_value_count / total_value_rows * 100) if total_value_rows > 0 else 0.0

    coverage_msg = (
        f"copy-from column: {copy_from}\n"
        f"total source1 rows: {total_value_rows:,}\n"
        f"missing values: {missing_value_count:,} ({missing_pct:.1f}%)\n"
        f"blank values: {empty_value_count:,} ({empty_pct:.1f}%)\n\n"
        "Action: Rows with missing/blank copy-from will result in empty enrichment values."
    )
    print_check("CHECK 3 - COPY-FROM COLUMN COVERAGE", coverage_msg)

    # Print PK values (join_left) for rows where the copy-from value is missing/blank
    if missing_value_count > 0 or empty_value_count > 0:
        try:
            missing_mask = s1[copy_from].isna() | (s1[copy_from].fillna("").str.strip() == "")
            missing_keys = s1.loc[missing_mask, join_left].astype(str)
            unique_missing = list(dict.fromkeys(missing_keys.tolist()))
            n_missing = len(unique_missing)
            max_show = 200
            shown = unique_missing[:max_show]
            more = n_missing - len(shown)
            miss_msg = f"Rows in source1 with missing/blank {copy_from} (showing {len(shown)} of {n_missing}): {shown}"
            if more > 0:
                miss_msg += f" ... and {more} more"
            print_check("FAILED KEYS - MISSING_COPY_FROM", miss_msg)
        except Exception:
            pass

    # ---------------------------------------------------------------------
    # Check 4: Consistency / one-to-one mapping risk
    # ---------------------------------------------------------------------
    # If a source2 join key maps to more than one source1 row, the join is ambiguous.
    ambiguous_keys = key_counts[key_counts > 1]
    ambiguous_source2_keys = source2_keys[source2_keys.isin(ambiguous_keys.index)]
    ambiguous_count = int(ambiguous_source2_keys.shape[0])
    ambiguous_pct = (ambiguous_count / total_source2_keys * 100) if total_source2_keys > 0 else 0.0

    if ambiguous_count == 0:
        consistency_msg = "No ambiguous mappings detected between source2 and source1."
    else:
        consistency_msg = (
            f"Ambiguous source2 rows: {ambiguous_count:,} ({ambiguous_pct:.1f}%)\n"
            "These source2 rows point to duplicate source1 keys and would not map cleanly.\n\n"
            "Action: Resolve duplicate keys in source1 or accept first-match behavior."
        )

    print_check("CHECK 4 - JOIN CONSISTENCY", consistency_msg)

    # Print the join keys in source2 that are ambiguous (point to duplicated source1 keys)
    if ambiguous_count > 0:
        try:
            amb_mask = s2[join_right].notna() & s2[join_right].isin(duplicate_keys.index)
            amb_keys = s2.loc[amb_mask, join_right].astype(str)
            unique_amb = list(dict.fromkeys(amb_keys.tolist()))
            n_amb = len(unique_amb)
            max_show = 200
            shown = unique_amb[:max_show]
            more = n_amb - len(shown)
            amb_msg = f"Ambiguous source2 join values ({n_amb} total): {shown}"
            if more > 0:
                amb_msg += f" ... and {more} more"
            print_check("FAILED KEYS - AMBIGUOUS_SOURCE2_VALUES", amb_msg)
        except Exception:
            pass

    # Concise, machine-readable style summary for quick scanning
    summary_line = (
        f"unmatched={unmatched_count:,} | duplicate_keys={duplicate_count:,} | "
        f"missing_copy_from={missing_value_count:,} | ambiguous={ambiguous_count:,}"
    )
    print_check("VALIDATION SUMMARY", summary_line)

    # A brief overall outcome to make the console output easier to interpret.
    if duplicate_keys.empty and missing_value_count == 0 and ambiguous_count == 0:
        print("\nValidation result: OK - the join looks suitable for enrichment.")
    else:
        print(
            "\nValidation result: Issues found. Review duplicate keys, missing values, "
            "and ambiguous mappings before using the output file."
        )

    # Build a structured results dict for programmatic consumption and optional samples.
    results: Dict[str, Any] = {}
    results["counts"] = {
        "source1_rows": len(source1),
        "source2_rows": len(source2),
        "total_source2_keys": total_source2_keys,
        "match_count": match_count,
        "unmatched_count": unmatched_count,
        "duplicate_count": duplicate_count,
        "missing_value_count": missing_value_count,
        "empty_value_count": empty_value_count,
        "ambiguous_count": ambiguous_count,
    }

    # Recompute small lists for returning (deduped, ordered)
    try:
        set_source1_keys = set(source1_keys)

        unmatched_mask = s2[join_right].notna() & ~s2[join_right].isin(set_source1_keys)
        unmatched_keys = s2.loc[unmatched_mask, join_right].astype(str)
        unique_unmatched = list(dict.fromkeys(unmatched_keys.tolist()))

        dup_keys_list = [str(k) for k in duplicate_keys.index.tolist()]

        missing_mask = s1[copy_from].isna() | (s1[copy_from].fillna("").str.strip() == "")
        missing_keys = s1.loc[missing_mask, join_left].astype(str)
        unique_missing = list(dict.fromkeys(missing_keys.tolist()))

        amb_mask = s2[join_right].notna() & s2[join_right].isin(duplicate_keys.index)
        amb_keys = s2.loc[amb_mask, join_right].astype(str)
        unique_amb = list(dict.fromkeys(amb_keys.tolist()))

        # Trim lists returned for readability
        max_return = max(25, sample_size)
        results.update(
            {
                "unmatched_keys": unique_unmatched[:max_return],
                "duplicate_keys": dup_keys_list[:max_return],
                "missing_keys": unique_missing[:max_return],
                "ambiguous_keys": unique_amb[:max_return],
            }
        )

        if return_samples:
            # Include small sample DataFrames
            results["sample_unmatched_df"] = s2.loc[unmatched_mask].head(sample_size).reset_index(drop=True)
            results["sample_duplicate_df"] = s1.loc[s1[join_left].isin(duplicate_keys.index)].head(sample_size).reset_index(drop=True)
            results["sample_missing_df"] = s1.loc[missing_mask].head(sample_size).reset_index(drop=True)
            results["sample_ambiguous_df"] = s2.loc[amb_mask].head(sample_size).reset_index(drop=True)
    except Exception:
        # If anything goes wrong building samples, still return counts
        pass

    return results


def enrich_csv(
    source1_path: Path,
    source2_path: Path,
    join_left: str,
    join_right: str,
    copy_from: str,
    new_column: str,
    write_samples: bool = False,
    sample_size: int = 25,
    samples_dir: Optional[Path] = None,
) -> Path:
    """Load the CSVs, validate the join, enrich source2, and write the result.

    Parameters added:
    - `write_samples`: when True, write small CSV samples for failing checks.
    - `sample_size`: number of rows to include in each sample CSV.
    - `samples_dir`: directory to write sample CSVs (defaults to parent of `source2_path`).

    Returns the output path so the caller can display it.
    """
    source1 = pd.read_csv(source1_path)
    source2 = pd.read_csv(source2_path)

    # Run validations first so the script fails fast if the assumptions are wrong.
    results = validate_inputs(
        source1, source2, join_left, join_right, copy_from, sample_size=sample_size, return_samples=write_samples
    )

    # Optionally write sample CSVs for failing checks (unmatched/duplicate/missing/ambiguous)
    if write_samples:
        out_dir = Path(samples_dir) if samples_dir is not None else source2_path.parent
        out_dir.mkdir(parents=True, exist_ok=True)
        written = []
        try:
            if "sample_unmatched_df" in results and not results["sample_unmatched_df"].empty:
                p = out_dir / f"{source2_path.stem}_unmatched_{join_right}_sample.csv"
                results["sample_unmatched_df"].to_csv(p, index=False)
                written.append(p)
            if "sample_duplicate_df" in results and not results["sample_duplicate_df"].empty:
                p = out_dir / f"{source1_path.stem}_duplicate_{join_left}_sample.csv"
                results["sample_duplicate_df"].to_csv(p, index=False)
                written.append(p)
            if "sample_missing_df" in results and not results["sample_missing_df"].empty:
                p = out_dir / f"{source1_path.stem}_missing_{copy_from}_sample.csv"
                results["sample_missing_df"].to_csv(p, index=False)
                written.append(p)
            if "sample_ambiguous_df" in results and not results["sample_ambiguous_df"].empty:
                p = out_dir / f"{source2_path.stem}_ambiguous_{join_right}_sample.csv"
                results["sample_ambiguous_df"].to_csv(p, index=False)
                written.append(p)
        except Exception:
            pass
        if written:
            for p in written:
                print(f"Wrote sample file: {p}")

    # Keep only the join key and the value to copy from source1.
    lookup = source1[[join_left, copy_from]].copy()
    lookup[join_left] = lookup[join_left].astype("string")
    lookup[copy_from] = lookup[copy_from].astype("string")

    # If source1 has duplicate join keys, keep the first occurrence for the join.
    # This avoids exploding rows during merge while still allowing the issue to be flagged.
    lookup = lookup.drop_duplicates(subset=[join_left], keep="first")

    enriched = source2.copy()
    enriched[join_right] = enriched[join_right].astype("string")
    lookup[join_left] = lookup[join_left].astype("string")

    # Left join preserves all rows in source2.
    merged = enriched.merge(
        lookup,
        how="left",
        left_on=join_right,
        right_on=join_left,
        suffixes=("", "_lookup"),
    )

    # Populate the requested new column from the matched source1 value.
    merged[new_column] = merged[copy_from]

    # Remove helper columns created by the merge.
    drop_cols = [col for col in [join_left, copy_from] if col in merged.columns]
    merged = merged.drop(columns=drop_cols, errors="ignore")

    # Derive the final output path automatically.
    output_path = derive_output_path(source2_path)
    merged.to_csv(output_path, index=False)

    # Final summary for the user.
    matched_rows = int(merged[new_column].notna().sum())
    unmatched_rows = int(merged[new_column].isna().sum())
    print("\nOutput written successfully.")
    print(f"Source file 2: {source2_path}")
    print(f"Output file: {output_path}")
    print(f"Matched rows: {matched_rows:,}")
    print(f"Unmatched rows: {unmatched_rows:,}")

    return output_path


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line interface."""
    parser = argparse.ArgumentParser(
        description=(
            "Enrich a CSV file by joining it to a lookup CSV and copying a value "
            "into a new column."
        )
    )
    parser.add_argument("--source1", required=True, help="Path to the lookup/source CSV file.")
    parser.add_argument("--source2", required=True, help="Path to the CSV file to enrich.")
    parser.add_argument(
        "--join",
        required=True,
        help='Join condition in the form "source1_column=source2_column".',
    )
    parser.add_argument(
        "--copy-from",
        required=True,
        help="Column name in source1 to copy into the new output column.",
    )
    parser.add_argument(
        "--new-column",
        required=True,
        help="Name of the new column to populate in the output file.",
    )
    parser.add_argument(
        "--write-samples",
        action="store_true",
        help="Write small CSV samples for failed checks (unmatched/duplicate/missing/ambiguous).",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=25,
        help="Number of sample rows to capture/write for failures (default: 25).",
    )
    parser.add_argument(
        "--samples-dir",
        type=Path,
        default=None,
        help="Directory to write sample CSVs; defaults to the parent directory of --source2.",
    )
    return parser


def main() -> int:
    """CLI entry point."""
    parser = build_parser()
    args = parser.parse_args()

    try:
        join_left, join_right = parse_join_expression(args.join)
        enrich_csv(
            source1_path=Path(args.source1),
            source2_path=Path(args.source2),
            join_left=join_left,
            join_right=join_right,
            copy_from=args.copy_from,
            new_column=args.new_column,
            write_samples=getattr(args, "write_samples", False),
            sample_size=getattr(args, "sample_size", 25),
            samples_dir=getattr(args, "samples_dir", None),
        )
        return 0
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
