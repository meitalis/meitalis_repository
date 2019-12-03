#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# In[ ]:


np.array([1, 2, 3, 4])

# In[ ]:


# In[ ]:


np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

# In[ ]:


np.zeros((3, 2))

# In[ ]:


a = [1, 2, 3, 4]
np.ones_like(a)

# In[ ]:


np. * np.zeros(3)

# In[ ]:


# In[ ]:


np.nan * np.zeros(3)

# In[ ]:


np.array([[1, 2, 3], np.ones(3)])

# In[ ]:


np.linspace(0, 1000, 6)

# In[ ]:


# Create a 3 × 3 matrix with values ranging from 0 to 8
Create
a
Hilbert
matrix
of
size
N × N(N is given
by
the
user))
np.array(range(9))
a.shape = (3, 3)
a

# In[ ]:


# Create an array with values ranging from 10 to 49
np.array(range(10, 50))

# In[ ]:


# Create a vector of size 10 containing only zeros of integer type
v = np.zeros(10, dtype=int)
v

# In[ ]:


# Create a Hilbert matrix of size N × N (N is given by the user)


# In[ ]:


# In[50]:


import numpy as np

n = 3
matrix = np.zeros([n, n])
x = 0
y = 1

matrix[x, y] = 1
for i in range(2, 10):
    xt, yt, x, y = x, y, (x - 1) % n, (y + 1) % n

if matrix[x, y] != 0:
    x = (xt + 1) % n
y = yt

print(i, "x", x, "y", y)

matrix[x, y] = i

matrix

# In[55]:


a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[1, 0], [0, 1]])
print(b)

# In[56]:


a = np.array([[1, 2], [3, 4]])
print(a)
b = np.array([[1, 0], [0, 1]])
print(b)

# In[61]:


a = np.array([[1, 2], [3, 4]])
# print(a)
b = np.array([[1, 0], [0, 1]])
# print(b)

a * b
# c = a@b
# j = a.dot(b)
# print("j",j)


# In[64]:


a = np.array([[1, 2, 3, 4]])
a.resize((2, 2))
a

# In[70]:


b = np.array([[1, 2], [3, 4]])
b.flatten()

# In[72]:


c = np.array([[1, 2], [3, 4]])
c.ravel()

