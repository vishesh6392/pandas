import pandas as pd

data={
    'name':['john',None,'peter','jeff','bill','lisa','jose'],
    'age':[23,78,None,19,45,33,20],
    'salary':[50000,None,42000,44000,39000,25000,45000],
    'performance score' :[4.5,3.4,3.9,4.7,4.2,4.6,3.8]
}

df=pd.DataFrame(data)
print(df)
# check ??
print(df.isnull())
print("count of null values")
print(df.isnull().sum())
# hndle missing -> df.dropna(axis,inplace)
# df.dropna(axis=0,inplace=True)
# print(df)

# fill ->df.fillna(value,inplace)
# df['age']=df['age'].fillna(df['age'].mean())
# print(df)

# best way->use interploation
# # why-> 1.preserve data integrity
#         2.smooth trends
#         3. avoid data loss 
#         4.use for time series data
df['age']=df['age'].interpolate(method='linear')
print(df)
'''
 1-timer series data
 2-numeric data with trends
 3- avoid droping row
 dis-> not use with catorogical data
'''