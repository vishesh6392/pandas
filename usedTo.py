# clm ,rows?
# what type of?
# missing Data
# info()->method
#-> 1-num of row and col 
#->2- col name
#->3- int64 float64 object
#->not null counts
#-> memory uses
import pandas as pd
df=pd.read_csv("sales_data_sample.csv",encoding='latin1')
print(df.info())