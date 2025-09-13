
import pandas as pd

data={
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,23,23,45,33,20],
    'salary':[50000,54000,42000,44000,39000,25000,45000],
}
df=pd.DataFrame(data)
print(df)
# df.sort_values(by=['age','salary'],ascending=[True,False],inplace=True)
# print(df)

grouped=df.groupby(['age','name'])['salary'].sum()
print(grouped)

'''
aggression funt
1-sum()
2-mean()
3-max()
4-min()
5-count()
6-std()
7-var()
8-median()
'''

 