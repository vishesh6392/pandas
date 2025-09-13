#step-2
import pandas as pd
data={
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'salary':[50000,54000,42000,44000,39000,25000,45000],
    'performance score' :[4.5,3.4,3.9,4.7,4.2,4.6,3.8]
}
df=pd.DataFrame(data)
print("sample dataframe")
print (df)
# print(df['name']) # single col
# print(df[['name','age']]) # multiple col

# print(df[df['salary']>40000])
# print(df[(df['age']>30 ) & (df['salary']>40000)])
# print(df[(df['age']>30 ) | (df['salary']>50000)])

# update->
df['salary']=df['salary']*1.1
#insert
df['bonus']=df['salary']*0.1
df.insert(0,'id',[101,102,103,104,105,106,107])
#update by loc
# df.loc[row_i,'col name']=new value
df.loc[0,'salary']=55000

# remove df.drop(col=['colname'],inplace=true)
df.drop(columns=['bonus'],inplace=True)
print(df)

