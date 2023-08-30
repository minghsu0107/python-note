import numpy as np
import pandas as pd

# mydf = pd.read_csv("mydf.csv", index_col="myindexcol")

s1 = pd.Series([4, 5, 6], index=["one", "two", "three"])
print(s1[s1 > 4])
'''
two      5
three    6
dtype: int64
'''

df = pd.DataFrame({'pre_month': [1, 4, 7, 10],
                   'pre_year': [2012, 2014, 2013, 2014],
                   'pre_sale': [55, 40, 84, 31]})
'''
   pre_month  pre_year  pre_sale
0          1      2012        55
1          4      2014        40
2          7      2013        84
3         10      2014        31
'''

df.columns = df.columns.str.replace('^pre_', '', regex=True)
print(df[df['month'] >= 4]['sale']) # return pd.Series
'''
dtype: int64
1    40
2    84
3    31
Name: sale, dtype: int64
'''
print(df[df['month'] >= 4]['sale'].values) # python list
print(df[df['year'].isin([2014])]) # return pd.DataFrame
'''
   month  year  sale
1      4  2014    40
3     10  2014    31
'''

df.set_index('month', inplace=True)
for idx in df.index:
    print(idx)
print(list(df.index))  # [1, 4, 7, 10]

# return iloc indices
print(np.where(df.index >= 7)[0])  # np.array([2, 3])

print(df.loc[10]['year'])  # 2014
print(df.loc[10, 'year'])  # 2014

ser = df.loc[[4, 7], 'year']  # returns pd.Series (it's iterable)
print(ser)
'''
month
4     2014
7     2013
Name: year, dtype: int64
'''
print(ser[7])  # 2013

print(df.iloc[0]['year'])  # 2012
print(df.iloc[0])  # returns pd.Series

print(list(df.iloc[0]))  # [2012, 55]

# pd.Series.map: apply changes on each entry in pd.Series
# returns a new pd.Series object
print(df[df['year'].map(lambda row: row in {2013, 2014})])
'''
       year  sale
month
4      2014    40
7      2013    84
10     2014    31
'''

df = pd.DataFrame({'key': ['K0', 'K1', 'K2', 'K3', 'K4', 'K5'],
                   'A': ['A0', 'A1', 'A2', 'A3', 'A4', 'A5']})

other = pd.DataFrame({'key': ['K0', 'K1', 'K2'],
                      'B': ['B0', 'B1', 'B2']})

# use join when you want to join by index
# DataFrame.join(self, other, on=None, how='left', lsuffix='', rsuffix='', sort=False) -> DataFrame
# on=None: joins index-on-index by default
# sort: Order result DataFrame lexicographically by the join key.
# If False, the order of the join key depends on the join type (how keyword).
print(df.join(other, lsuffix='_caller', rsuffix='_other'))
print(df.set_index('key').join(other.set_index('key')))
# preserves the original DataFrame’s index
print(df.join(other.set_index('key'), on='key'))
'''
df:
  key   A
0  K0  A0
1  K1  A1
2  K2  A2
3  K3  A3
4  K4  A4
5  K5  A5
other:
  key   B
0  K0  B0
1  K1  B1
2  K2  B2
  key_caller   A key_other    B
0         K0  A0        K0   B0
1         K1  A1        K1   B1
2         K2  A2        K2   B2
3         K3  A3       NaN  NaN
4         K4  A4       NaN  NaN
5         K5  A5       NaN  NaN
      A    B
key
K0   A0   B0
K1   A1   B1
K2   A2   B2
K3   A3  NaN
K4   A4  NaN
K5   A5  NaN
  key   A    B
0  K0  A0   B0
1  K1  A1   B1
2  K2  A2   B2
3  K3  A3  NaN
4  K4  A4  NaN
5  K5  A5  NaN
'''

# Dataframe of number of sales made by an employee
sales = {'Tony': 103,
         'Sally': 202,
         'Randy': 380,
         'Ellen': 101,
         'Fred': 82
         }
# Dataframe of all employees and the region they work in
region = {'Tony': 'West',
          'Sally': 'South',
          'Carl': 'West',
          'Archie': 'North',
          'Randy': 'East',
          'Ellen': 'South',
          'Fred': np.nan,
          'Mo': 'East',
          'HanWei': np.nan,
          }

sales_df = pd.DataFrame.from_dict(sales, orient='index',
                                  columns=['sales'])
region_df = pd.DataFrame.from_dict(region, orient='index',
                                   columns=['region'])
print(sales_df)
print(region_df)
'''
       sales
Tony     103
Sally    202
Randy    380
Ellen    101
Fred      82
       region
Tony     West
Sally   South
Carl     West
Archie  North
Randy    East
Ellen   South
Fred      NaN
Mo       East
HanWei    NaN
'''
# use merge when you want to join on columns other than index
# left_index=True: join on left index, same for right_index=True
joined_df_merge = region_df.merge(
    sales_df, how='left', left_index=True, right_index=True)
print(joined_df_merge)
# same as region_df.join(sales_df, how='left') in here
'''
       region  sales
Tony     West  103.0
Sally   South  202.0
Carl     West    NaN
Archie  North    NaN
Randy    East  380.0
Ellen   South  101.0
Fred      NaN   82.0
Mo       East    NaN
HanWei    NaN    NaN
'''
demo = joined_df_merge.copy()
# demo['sales'] = demo['sales'].fillna(demo['sales'].mean())
# demo['sales'] = demo['sales'].fillna(demo['sales'].median())
demo.dropna(inplace=True)
print(demo)
'''
      region  sales
Tony    West  103.0
Sally  South  202.0
Randy   East  380.0
Ellen  South  101.0
'''

grouped_df = joined_df_merge.groupby(by='region').sum()
grouped_df.reset_index(inplace=True)  # set index to 0, 1, 2...
print(grouped_df)
'''
  region  sales
0   East  380.0
1  North    0.0
2  South  303.0
3   West  103.0
'''

employee_contrib = joined_df_merge.merge(grouped_df, how='left',
                                         left_on='region',
                                         right_on='region',
                                         suffixes=('', '_region'))

print(employee_contrib)
'''
  region  sales  sales_region
0   West  103.0         103.0
1  South  202.0         303.0
2   West    NaN         103.0
3  North    NaN           0.0
4   East  380.0         380.0
5  South  101.0         303.0
6    NaN   82.0           NaN
7   East    NaN         380.0
8    NaN    NaN           NaN
'''
employee_contrib = employee_contrib.set_index(joined_df_merge.index)
employee_contrib = employee_contrib.dropna(subset=['region'])
employee_contrib = employee_contrib.fillna({'sales': 0})
employee_contrib['%_of_sales'] = employee_contrib['sales'] / \
    employee_contrib['sales_region']
print(employee_contrib[['region', 'sales', '%_of_sales']]
      .sort_values(by=['region', '%_of_sales']))
'''
       region  sales  %_of_sales
Mo       East    0.0    0.000000
Randy    East  380.0    1.000000
Archie  North    0.0         NaN
Ellen   South  101.0    0.333333
Sally   South  202.0    0.666667
Carl     West    0.0    0.000000
Tony     West  103.0    1.000000
'''
