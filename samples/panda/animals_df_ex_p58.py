#!/usr/bin/env python
# coding: utf-8

# In[62]:


import pandas as pd
import numpy as np


# In[206]:


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
animals_df = pd.DataFrame(data,index=labels)
animals_df


# In[229]:



# Return the first 3 rows of the DataFrame
dft2 = animals_df[0:3]
dft3 = animals_df.iloc[0:3,:]
animals_df.head(3)

#animals_df.shape
#animals_df.shape[0] same as len(animals_df)
#animals_df.shape[1]

# dft2 = animals_df.loc['a':'e']
# dft2
# dft2.loc['a','animal'] = 'ct'
# dft.iloc[1,1] = 5555 
# dft.loc['a','animal'] = 'cattttt'

dft4 = animals_df.iloc[:3]
dft4



# In[165]:


animals_df.isna()


# In[168]:


animals_df.isna().sum()


# In[173]:


animals_df.describe()
animals_df.describe().T


# In[180]:


# select the number of visits of the animal in row 'd'
animals_df.loc['d','visits']
animals_df.at['d','visits']


# In[230]:


get_ipython().run_line_magic('rerun', '206')

dft2 = animals_df.loc['a':'e']
print("**** dt2 before change ***")
print(dft2)

dft2.iloc[1,1] = 6666
print("\n**** dt2 after iloc 6666 ***")
print(dft2)
print("\n**** animals_df after iloc 6666 ***")
print(animals_df)


dft2.iat[0,0] = 'dfsdfsdf'
print(dft2)
print(animals_df)


# In[204]:


# Select the data in rows ['b', 'e'] and in columns ['animal', 'age']
animals_df.iloc[[1,4],[0,1]]
animals_df.loc[['b', 'e'],['animal','age']]


# In[203]:


#Select the data in rows [3, 4, 8] and in columns ['animal', 'age']
i2 = animals_df.index.values[[3,4,8]]
animals_df.loc[i2,['animal','age']]

# animals_df.iloc[[3, 4, 8],[0,1]]


# In[211]:


# Select the rows where the number of visits is greater than 2
# animals_df.loc[:,'visits']
# animals_df[animals_df.loc[:,'visits'] > 2]

animals_df[animals_df.visits > 2]


# In[212]:


animals_df[animals_df.visits > 2].visits


# In[217]:


# Select the rows where the animal is a cat and the age is less than 3
animals_df[(animals_df.loc[:,'animal']=='cat') & (animals_df.loc[:,'age'] < 3)]
animals_df[(animals_df.animal =='cat') & (animals_df.age <3 )]


# In[223]:


#Select the rows where the age is missing, i.e. is NaN
animals_df.isna().loc[:,'age']
animals_df[animals_df.isna().loc[:,'age']]
#animals_df[animals_df.loc[:,'age']]

#animals_df[np.isnan(animals_df.age)]


# In[219]:


#Change the age in row 'f' to 1.5
animals_df.at['f','age'] = 1.5


# In[ ]:




