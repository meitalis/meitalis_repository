#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# Q1

# In[2]:


a = np.linspace(2, 5, 5)
print(a)


# In[3]:


a = np.arange(12).reshape(4, 3)
print(a[1:3])


# In[4]:


a = np.arange(12).reshape(3, 4)
print(a[:, ::-1])


# In[5]:


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([0, 10, 100])
print(a * b)


# In[6]:


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([0, 10, 100])
print(np.dot(a, b))


# In[7]:


a = np.arange(1, 6)
print(np.vstack((a, a ** 2, a ** 3)).T)


# In[4]:


a = np.array([[1,3,4], [2,3,5], [0,1,-1]])
print(a@a)
print(a@a@a)


# In[3]:


a = np.arange(8).reshape((4, 2))
a = np.insert(a, 2, 0, axis=1)
print(a)


# In[5]:


dtype = [('name', 'S10'), ('height', 'f4'), ('age', 'i4')]
values = [('Arthur', 1.8, 41), ('Lancelot', 1.9, 38), ('Galahad', 1.7, 38)]
a = np.array(values, dtype=dtype) 
a['height'][1]


# In[11]:


from numpy.polynomial import Polynomial
p = Polynomial([4, 5, 1, 2])
print(p.deriv(3))


# Q2

# In[12]:


def even_(arr):
    even = (a % 2 == 0) & ~(a % 10 == 0)
    return arr[even] 


# In[13]:


a = np.array([4, 2, 7, 11, 8, 5, 10, 14])
print(a)
print(even_(a))


# Q3

# In[14]:


def count_rows(arr, num):
    return np.sum(np.any(arr == num, axis=1))      


# In[15]:


a = np.array([[5, 2, 7, 6], [8, 3, 0, 3], [1, 7, 3, 7], [0, 2, 1, 2]])
print(a)


# In[16]:


print(count_rows(a, 7))


# Q4

# In[11]:


a = np.array([[10, 12, 7, 3, 12], 
              [3, 10, 6, 2, 8],
              [18, 24, 17, 6, 10],
              [15, 21, 10, 8, 12],
              [1, 18, 22, 4, 15]])
print(a)


# In[18]:


cols_min = np.argmin(a, axis=0)
cols_max = np.argmax(a, axis=0)

rows_min = np.argmin(a, axis=1)
rows_max = np.argmax(a, axis=1)
    
number_or_row = np.arange(a.shape[0])

idx1 = np.where(rows_max[cols_min[number_or_row]] == number_or_row)[0]
idx2 = np.where(rows_min[cols_max[number_or_row]] == number_or_row)[0]
    
saddle1 = a[idx1, cols_min[idx1]]
saddle2 = a[idx2, cols_max[idx2]]

print(saddle1)
print(saddle2)


# In[19]:


a


# In[49]:


cols_max = np.argmax(a, axis=0)

cols_max


# In[50]:


number_or_row = np.arange(a.shape[0])

number_or_row


# In[30]:


cols_max[number_or_row]


# In[51]:


rows_min = np.argmin(a, axis=1)
rows_min


# In[32]:


rows_min[cols_max[number_or_row]]


# In[33]:


#take the row that is a valid intersection
rows_min[cols_max[number_or_row]] == number_or_row


# In[46]:


#now we have a valid intersection, take the row by np.where...
idx2 = np.where(rows_min[cols_max[number_or_row]] == number_or_row)
idx2


# In[47]:


#grab by row and column
saddle2 = a[idx2, cols_max[idx2]]


# In[45]:


saddle2


# In[ ]:




