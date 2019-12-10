#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np


# In[ ]:


data = pd.Series([0.2,0.5,0.75,1])


# In[ ]:


data


# In[ ]:


data.index


# In[ ]:


data.values


# In[ ]:


type(data.values)


# In[ ]:


data.index.values


# In[ ]:


a = data[(data>=0.5) & (data<=0.75)]


# In[ ]:


type(a)


# In[ ]:


data = pd.Series([0.2,0.5,0.75,1],
                    index='a b c d'.split())
data


# In[ ]:


l = list('abcd')
print(l)
data = pd.Series([0.2,0.5,0.75,1],
                    index=l)

data


# In[ ]:


data['c'] = 0.8
data


# In[ ]:


data['x'] = 333
data


# In[ ]:


data = pd.Series([0.25,0.5,0.75,1],
                    index=[2,3,5,7])
data


# In[ ]:


data[2]


# In[ ]:


data.index=[1,3,5,7]
data


# In[ ]:


poulation_dict = {'Ca':397,
                  'Te':287,
                  'Fl':213,
                  'NY':198,
                  'Pe':128}

poulation = pd.Series(poulation_dict)
poulation


# In[ ]:


area_dict = {'CC':3947,
                  'Te':2487,
                  'Fl':2143,
                  'NY':1498,
                  'Pe':1428}

area = pd.Series(area_dict)
area


# In[ ]:


df = pd.DataFrame({'poulation':poulation,
                       'area':area
    
})

df


# In[ ]:


df.head(2)


# In[ ]:


df.tail(2)


# In[ ]:



df.info()


# In[ ]:


df.index


# In[ ]:


df.columns


# In[ ]:


type(df['poulation'])


# In[ ]:


df['poulation']['CC']


# In[ ]:


df4 = pd.DataFrame(data)


# In[ ]:


df4


# In[ ]:


a = pd.DataFrame(


# In[ ]:


data = {'population':[397,287,555,666,777],
        'area':[3947,2847,5455,4666,4777]}
index = ['CC', 'Ca', 'Fl', 'NY', 'Pe']
df = pd.DataFrame(data,index = index)
df


# In[ ]:


df2 = df[['area']]
df2


# In[ ]:


dtype = [("AMZN","f8"),("FB","f8"),("GOOG","f8")]
indexes = ['Closing price','EPS','Shares','Beta','PE','Market Cap(B)']
values = [(2039.51,171.16,1197.00),(12.63,6.46,23.16),(487.74,2398.61,348.95),(1.61,0.66,1.40),(15.98,25.87,51.38),(972.96,482.68,829.37)]
a = np.array(values,dtype=dtype)
df = pd.DataFrame(a,index=indexes)
df


# In[ ]:


cols = ['AMZN','FB','GOOG']
indexes = ['Closing price','EPS','Shares','Beta','PE','Market Cap(B)']
values = [(2039.51,171.16,1197.00),(12.63,6.46,23.16),(487.74,2398.61,348.95),(1.61,0.66,1.40),(15.98,25.87,51.38),(972.96,482.68,829.37)]
df = pd.DataFrame(values,columns=cols, index=indexes)
df


# In[ ]:


df[-2:-1]


# In[ ]:


f = lambda x: x.max()-x.min()


# In[ ]:





# In[ ]:


df.apply(f,axis=1)


# In[ ]:


df.apply(f,axis=1,result_type='expand')


# In[ ]:


df


# In[ ]:


df.apply(lambda x: [1, 2], axis=1)


# In[ ]:


data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
animals_df = pd.DataFrame(data,index=labels)
animals_df


# In[ ]:


animals_df = pd.DataFrame(data,index=labels)
animals_df


# In[ ]:


animals_df[['animal','age']]
animals_df[::-1]
animals_df[::2]
animals_df[2:]
animals_df.iloc[:,-1]


# In[ ]:


animals_df.iloc[2]


# In[ ]:


animals_df.iloc[1,1]
animals_df.iloc[[1,4],0:3]


# In[ ]:


animals_df.loc[:,'animal':'visits'].values


# In[ ]:


animals_df.loc['a':'d',:]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


import numpy as np
np_array = np.array([[1,2,3], [4,5,6] , [7,8,9], [10, 11, 12]])
test_array = np.array([4,5,6])
print("Original Numpy array:")
print(np_array)
print("Searched array:")
print(test_array)
print("Index of the searched array in the original array:")
print(np.where((np_array == test_array)))
print(np.where((np_array == test_array).all(1))[0])


# In[ ]:




