#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[ ]:


fname = "student-data.txt"


# In[ ]:



dtype1 = np.dtype([("gender","S1"),("height","f8")])
students = np.loadtxt(fname,dtype1,skiprows=9,usecols=(1,3))
students


# In[ ]:


males = students["gender"] == b'M'


# In[ ]:



print(students["height"])
print(students["height"][males])


# In[ ]:


males_avg = students["height"][males].mean()
males_avg 


# In[ ]:


fmales_avg = students["height"][~males].mean()
fmales_avg 


# In[ ]:


print("Male avg: {:.2f}m, fMale avg: {:.2f}m".format(males_avg,fmales_avg))


# In[ ]:


def parse_weight(s):
        try:
            return float(s)
        except ValueError:
            return -99


# In[ ]:


dtype2 = np.dtype([("gender","S1"),("weight","f8")])
students3 = np.loadtxt(fname,dtype2,skiprows=9,usecols=(1,4),converters={4:parse_weight})
students3


# In[ ]:


males = students3["gender"] == b'M'
valid = students3["weight"] > 0 
males_avg = students3["weight"][valid & males].mean()
males_avg 
fmales_avg = students3["weight"][valid & ~males].mean()
fmales_avg 
print("Male avg: {:.2f}m, fMale avg: {:.2f}m".format(males_avg,fmales_avg))


# In[13]:


fname = "data.txt"
data = np.genfromtxt(fname,dtype="f8, i4, f8, i4", delimiter=',')
print(data)


# In[14]:


fname = "data.txt"
data = np.genfromtxt(fname,dtype="f8, i4, f8, i4", delimiter=',',
                    missing_values={1: '???' ,2: '???' },
                    filling_values={1: -999 ,2: -99, 3: 0})
print(data)


# In[ ]:




