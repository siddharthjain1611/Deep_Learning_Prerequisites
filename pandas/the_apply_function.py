# how to assign a new colimn value where each cell is derived from the values already in the row
# equivalent to for, except it's not so slow as for loop

from column_names import *
from datetime import datetime
print(df.head(10))

# convert in to a new objects

datetime.strptime('1949-05', '%Y-%m')

# day time column to contain day time objects

df['dt'] = df.apply(lambda row: datetime.strptime(row['month'], '%Y-%m'), axis = 1)

print(df.info())
