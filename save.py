import pandas as pd
data={
    'name':['john','mary','peter','jeff','bill','lisa','jose'],
    'age':[23,78,22,19,45,33,20],
    'city':['nagpur','mumbai','pune','nagpur','mumbai','pune','nagpur']
}
df=pd.DataFrame(data)
print(df)
#df.to_csv('mydata.csv',index=False)
#df.to_excel('mydata.xlsx',index=False)
#df.to_json('mydata.json')