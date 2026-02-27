import pandas as pd

# Task 1 Load the dataset into a DataFrame called df. 
# Set order_id as the row index at load time. Display the first 5 rows and the last 5 rows.

import pandas as pd

url = "https://drive.google.com/uc?id=1Mlu9r3afSGz5_02Y3wDJoQLpXszQXaIU"
df = pd.read_csv(url, index_col='order_id')
print(df.head())
print(df.tail())

# Task 2 Run a structural inspection of df. From the output, answer the following in a markdown cell:

#How many rows and columns does the dataset have?

rows, col = df.shape
print("Number of rows:", rows)
print("Number of columns:", col)

#Which columns have missing values and how many nulls does each have?

missing = df.isnull().sum()
print("Columns with missing values and with number of nulls:")
for col in missing.index:
  if missing[col] > 0:
    print(col, ':', missing[col])

#Which column needs a data type conversion before any date-based analysis, and what function would you use?

df.info()

#Reason - order_date column is currently stored as a string, For performing date-based operations like filtering, sorting, or extracting year/month/day, it must be converted to datetime format.
# The function used for this conversion is pd.to_datetime()

df['order_date'] = pd.to_datetime(df['order_date'])
print(df['order_date'])

#Task 3 Run a statistical summary of the numeric columns. From the output, answer the following in a markdown cell:

#What is the median unit_price?

print(f"Median unit_price: {df['unit_price'].median()}")

#Does unit_price appear to be skewed? Explain using values from the output.

df.describe()

# From above describe values, yes the unit_price column appears to be right-skewed.

# Mean = 20224.6

# Median = 2500

# Maximum = 85000

# Minimum = 499

# Since the mean is much larger than the median, a few high values (such as 85000) are pulling the average upward. 
# This indicates that the distribution is right-skewed