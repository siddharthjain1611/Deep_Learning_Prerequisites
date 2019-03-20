import pandas as pd

df = pd.read_csv('international_airline_passangers.csv', engine = 'python', skipfooter = 3)
# we skip 3 head rows \

df.columns

# reassign the column names and pass it a list

df.columns = ["month", "passangers"]
print(df.passangers) # the same as df['passangers']

# to add a new column

df['ones'] = 1
print(df.head()) # see there's a new row on the right side
