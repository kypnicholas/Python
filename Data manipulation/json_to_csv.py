import pandas as pd

# Read JSON file and convert to CSV
# df = pd.read_json('data.json', lines=True)        # lines=True for line-delimited JSON files
df = pd.read_json('data.json')                      # without lines=True for standard JSON files

df.to_csv('output.csv',  index=False)               # index=False to avoid writing row numbers
