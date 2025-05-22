import pandas as pd

data = {
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35],
    'city': ['NYC', 'LA', 'Chicago']
}
df = pd.DataFrame(data)

# Get all rows, just the 'name' column
print(df.loc[:, 'name'])


print(df.iloc[1:3, :])

# Build this DataFrame:
df1 = pd.DataFrame({
    'A': [10, 20, 30, 40, 50],
    'B': [5, 4, 3, 2, 1]
}, index=['a', 'b', 'c', 'd', 'e'])



# 1. Select row 'c' and column 'B'
print(df1.iloc[2, 1])
# 2. Select rows 'b' to 'd' and both columns
print(df1.iloc[1:3, :])
# 3. Select rows where A > 30
print(df1['A']>30)
# 4. Select rows where A > 20 and B < 3
print((df1['A']> 20) & (df1['B']< 20))