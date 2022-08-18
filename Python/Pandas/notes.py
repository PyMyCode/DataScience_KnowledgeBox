import pandas as pd

"""
df correspond to a dict of series objects
- key > columns/headers
- value > elements in the columns
"""

# creating a df from a csv file
df = pd.read_csv("example.csv")

# saving to a csv
df = pd.to_csv("example.csv")

# reading the first few rows
df.head()

# getting the columns
df.columns
# getting indices
df.index

# PULLNG INFORMATION
# making a subset
df = df[["column1, column2"]]

series = df["column1"]

# Purely integer-location based indexing for selection by position
df.iloc[1,2]

# slicing
sub_df = df.iloc[0:2,0:3]

# Access the column using the name
df.loc[1, "column name"]

# filtering
df1 = df[df["columns_name"] >= something]


"""
df["columns_name" >= something] gives a True and False dataframe
"""
# Basic Data Stats

df[["column"]].mean()
df[["column"]].median()
df[["column"]].max()
df[["column"]].quantile(q=0.25)

