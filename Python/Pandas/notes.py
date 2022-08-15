import pandas as pd

"""
df correspond to a dict
- key > columns/headers
- value > elements in the columns
"""

# creating a df from a csv file
df = pd.read_csv("example.csv")

# saving to a csv
df = pd.to_csv("example.csv")

# reading the first few heads
print(df.head())

# getting the columns
df.columns

# making a subset
df = df[column_list]

# Purely integer-location based indexing for selection by position
df.iloc[1,2]

# filtering
df1 = df[df["columns_name" >= something]]

"""
df["columns_name" >= something] gives a True and False dataframe
"""