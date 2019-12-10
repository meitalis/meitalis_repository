#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[ ]:


df = pd.DataFrame(np.arange(8).reshape(2,4), index=['three','one'],
                      columns=['d','b','a','c'])

df


# In[ ]:


df.sort_index()


# In[ ]:


df.sort_index(axis=1)


# In[ ]:


df.iat[0,0] = 9


# In[ ]:


df.sort_values(by='d')


# In[2]:


df = pd.DataFrame({'b':[4,7,-3,2], 'a':[0,1,0,1]})
df


# In[17]:


df.sort_values('b')
df.sort_values(['a','b'])
df.sort_values('b',ascending=False)
df.sort_values(['a','b'],ascending=False)
df.sort_values(['a','b'],ascending=[False,True])
df.sort_values(['a','b'],ascending=[False,True],inplace=True)


# In[18]:


df


# In[ ]:




