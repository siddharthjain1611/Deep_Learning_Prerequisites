# joins from SQL

import pandas as pd

# read tables

t1 = pd.read_csv('table1.csv')
t2 = pd.read_csv('table2.csv')

print(t1, '\n', t2)

# joins user_id columns using merge function

mer = pd.merge(t1, t2, on = 'user_id')

print(mer)

# it's also possible to do it this way

t1.merge(t2, on = 'user_id')
