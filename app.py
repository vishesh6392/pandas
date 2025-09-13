import pandas as pd;
# read data from csv file into a data frame
df=pd.read_csv("sales_data_sample.csv",encoding='latin1')
print(df)