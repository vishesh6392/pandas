'''
conbine- vertically(row-wise) axis=0
combine- horizontally(col-wise) axis=1
'''

import pandas as pd
data1={
    'name':['john','mary','peter','jeff','bill'],
    'age':[23,78,22,19,45]
}
data2={
    'name':['lisa','jose'],
    'age':[33,20]
}
df1=pd.DataFrame(data1)
df2=pd.DataFrame(data2) 

df_combined=pd.concat([df1,df2],axis=0)
print(df_combined)
df_combined=pd.concat([df1,df2],axis=1)
print(df_combined)