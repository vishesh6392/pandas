
import pandas as pd
data1={
    'customer_id':[1,2,3,4,5],
    'name':[
        'john','mary','peter','jeff','bill'
    
    ]
}
data2={
    'customer_id':[1,2,3],
    'orderAmt':[100,200,300]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2)

# merge 
df_merged=pd.merge(df1,df2,on='customer_id',how='inner')
print(df_merged)
df_merged=pd.merge(df1,df2,on='customer_id',how='outer')
print(df_merged)
df_merged=pd.merge(df1,df2,on='customer_id',how='left')
print(df_merged)
df_merged=pd.merge(df1,df2,on='customer_id',how='right')
print(df_merged)
# df_merged=pd.merge(df1,df2,on='customer_id',how='cross')
# print(df_merged) not valid