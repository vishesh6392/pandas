# sumary of data
import pandas as pd
data={
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'salary':[50000,54000,42000,44000,39000,25000,45000],
    'performance score' :[4.5,3.4,3.9,4.7,4.2,4.6,3.8]
}
df=pd.DataFrame(data)
print("sample dataframe")
print(df)
print("summary of  decriptive statistics")
print(df.describe())