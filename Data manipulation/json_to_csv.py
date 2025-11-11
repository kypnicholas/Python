import pandas as pd

df = pd.read_json('c:/Users/nkypri01/Downloads/data.json', lines=True)      # lines=True for line-delimited JSON files
# df = pd.read_json('c:/Users/nkypri01/Downloads/data.json')                # without lines=True for standard JSON files

df.to_csv('c:/Users/nkypri01/Downloads/output.csv',  index=False)           # index=False to avoid writing row numbers
