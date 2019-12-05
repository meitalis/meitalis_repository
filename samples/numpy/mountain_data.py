#!/usr/bin/env python
# coding: utf-8

# In[22]:


import numpy as np
from datetime import datetime


# In[23]:0


fname = "mountain-data.txt"


# In[75]:


str2date = lambda x: np.datetime64(datetime.strptime(x, '%d/%m/%Y')) if '-' not in x else np.datetime64('2001-01-01T00:00:00')
str2date('20/03/1977')
str2date('-')


# In[77]:


str2date = lambda x: np.datetime64(datetime.strptime(x, '%d/%m/%Y')) if '-' not in x else np.datetime64('2001-01-01T00:00:00')
dtype = np.dtype([("name","S20"),("height","i8"),("First ascent date","datetime64"),("First winter date","datetime64"),("locationN","S10"),("locationE","S10")])
data = np.genfromtxt(fname,dtype=dtype,skip_footer=1,skip_header=4,delimiter='\t', converters = {2: str2date,3: str2date} )
data


# In[ ]:




