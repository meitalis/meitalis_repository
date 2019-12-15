
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np
import re


# In[ ]:


# df = pd.read_excel('KOV785TZ111.xls')
# df.head(10)
#df.tail(10)

# df.dtypes

# cols = [1, 2, 4]
# df = pd.read_excel('KOV785TZ111.xls',usecols=cols)

# df = pd.read_excel('KOV785TZ111.xls',index_col=0)
# pd.options.display.max_columns = None # or pd.set_option('display.max_columns', None) #pd.set_printoptions(max_columns=500)
# df.head(10)

# print("Sum: ",df["SACH_MISHKL"].sum()) 
# print("Mean: ",df["SACH_MISHKL"].mean())
# print("Maximum: ",df["SACH_MISHKL"].max())
# print("Minimum: ",df["SACH_MISHKL"].min()) 

#df.insert(0, "column1", np.nan)

# df.drop('column1',axis=1,inplace=True)
# df.head(10)

#df = pd.read_excel('KOV785TZ111.xls',skiprows=5)

# s = df[["MHUG", "TZIUN34"]].sum()
# df_sum=pd.DataFrame(data=s)
# df_sum.T

# df[df["TAR_LEDA"]==13081975].head(10)

# df_sub = df.groupby('TAR_LEDA').count()
#df_sub.info()
#df_sub.columns


#df_sub.iloc[:, 2][df_sub.iloc[:, 2] > 1].sort_values(ascending=False)

#df[df["TAR_LEDA"].isin([1011945,13081975])].head(10)

#df.query('TAR_LEDA == ["1011945", "13081976"]').head(10)

#df[df['TAR_LEDA'] >= 13081976] #date is int . invalid. should be datetime


# In[69]:


df1 = pd.read_excel('KOV785TZ111.xls')


#pd.options.display.max_columns = None 
#print(df.head(10))
df2 = df1.filter(regex='^((?!TAV).)*$', axis=1)
df2.columns
# keys = list(df2.columns.get)
# type(keys)
# cols = [1,2,3,4]
# type(cols)
#df1 = df1[df1.columns[cols]]
#df1
#print(df2.head(10))

# pattern = r'TAV*'
# idx = re.search(pattern, df.columns) 
# idx
df3 = df1.filter(regex='(?!TAV)', axis=1)
df3.head(10)


# ////try it


df.info()
df.isna()
df.isna().sum()
df.describe()