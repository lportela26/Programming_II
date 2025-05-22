import pandas as pd

df = pd.DataFrame({
    'price': [10, 20, 30],
    'tax_rate': [0.05, 0.1, 0.2]
})

# Create a new column 'total_price' = price + price * tax_rate
# Do it using .apply() with a lambda

df['Total_price'] = df['price']*(1+df['tax_rate'])
print(df)


df2 = pd.DataFrame({'year': ['2021', '2022', '2023']})

# Convert the 'year' column to integers.
df2['year'] = df2['year'].astype(int)

df1 = pd.DataFrame({'date': ['2022-12-25', '2023-01-01', '2023-07-04']})

# 1. Convert the column to datetime
df1['date'] = pd.to_datetime(df1['date'])

# 2. Create a column called 'month' with the month number
df1['month'] = df1['date'].dt.month_name() 

# 3. Create a column 'weekday' with 0 = Monday ... 6 = Sunday
df1['day'] = df1['date'].dt.day_name()

print(df1)

df3 = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'city': ['NY', 'NY', 'Chicago', 'NY', 'Chicago'],
    'income': [50000, 60000, 70000, 80000, 90000]
})

df4 = df3.groupby('city')['income'].mean()
print(df4)


df5 = pd.DataFrame({'id': [1, 2], 'name': ['Alice', 'Bob']})
df6 = pd.DataFrame({'id': [2, 3], 'score': [95, 80]})

# Merge them on 'id' using:
# - inner join
df7 = pd.merge(df5, df6, on = 'id', how = 'inner')
print(df7)
# - left join
df8 = pd.merge(df5, df6, on = 'id', how = 'left')
# - outer join
df9 = pd.merge(df5, df6, on = 'id', how = 'right')

print(df7)
print(df8)
print(df9)


