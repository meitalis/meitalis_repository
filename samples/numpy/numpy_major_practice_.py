#!/usr/bin/env python
# coding: utf-8

# Import numpy as np and print the version number.

# In[1]:


import numpy as np
print(np.__version__)


# In[ ]:


# Create a 1D array of numbers from 0 to 9
# #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[ ]:


a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])




arr = np.arange(10)


# In[ ]:


a


# In[ ]:


# Create a 3×3 numpy array of all True’s


# In[ ]:


a = np.isclose(np.ones([3,3]),np.ones([3,3]))
print(a)
b = np.full((3,3),True)
b



np.full((3, 3), True, dtype=bool)
np.ones((3,3), dtype=bool)


# In[ ]:


# Extract all odd numbers from arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# #> array([1, 3, 5, 7, 9])


# In[ ]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 != 0]


arr[arr % 2 == 1]


# In[ ]:


# Replace all odd numbers in arr with -1

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


# In[ ]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[arr%2 != 0] = -1
arr


arr[arr % 2 == 1] = -1
arr


# In[ ]:


# Replace all odd numbers in arr with -1 without changing arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#hint - where


# In[ ]:


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
b = np.where(arr%2 != 0,-1,arr) 
print(arr) 
print(b) 


arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
out


# In[ ]:


# np.arange(10)

# #> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired Output:

# #> array([[0, 1, 2, 3, 4],
# #>        [5, 6, 7, 8, 9]])


# In[ ]:


arr = np.arange(10)
print(arr)
arr_2 = arr.reshape(2,5)
print(arr)
print(arr_2)
arr_3 = arr.resize(2,5)
print(arr)
print("arr_3",arr_3)


arr = np.arange(10)
arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols


# In[ ]:


# Stack arrays a and b vertically
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)


# In[27]:


a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
print(a)
print(b)
np.vstack((a,b))


a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.vstack([a, b])


# In[ ]:


# Get the common items between a and b
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# Desired Output:

# array([2, 4])


# In[28]:


# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# np.unique(a[np.isclose(a,b)])

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)


# In[ ]:


# Get the positions where elements of a and b match
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# Desired Output:

# #> (array([1, 3, 5, 7]),)


# In[ ]:


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

c = np.where(np.isclose(a,b))
c


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a == b)


# In[ ]:


# Get all items between 5 and 10 from a.
# a = np.array([2, 6, 1, 9, 10, 3, 27])
# Desired Output:

# (array([6, 9, 10]),)


# In[ ]:


a = np.array([2, 6, 1, 9, 10, 3, 27])
a[(a<=10) & (a>=5)]


a = np.array([2, 6, 1, 9, 10, 3, 27])

index = np.where((a >= 5) & (a <= 10))
a[index]

a[(a >= 5) & (a <= 10)]


# In[ ]:


# Reverse the rows of a 2D array arr.
# # Input
# arr = np.arange(9).reshape(3,3)


# In[29]:


arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[::-1])


# In[ ]:


# Reverse the columns of a 2D array arr. (last arr)


# In[30]:


arr = np.arange(9).reshape(3,3)
print(arr)
print(arr[:,::-1,])
      
    
arr[:, ::-1]


# In[ ]:


# Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.


# In[ ]:


aa = np.random.randint(5,10,(5,3))
aa


# In[ ]:


# Print or show only 3 decimal places of the numpy array rand_arr.
# hint: set_printoptions


# In[ ]:


np.set_printoptions(precision=3)
np.array([1.123456789,2.333333,6.555555])


# In[ ]:


# Limit the number of items printed in python numpy array a to a maximum of 6 elements.


# In[9]:


np.set_printoptions(threshold=4)
np.random.randint(5,10,(7,7))


# In[5]:


# From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
# np.random.seed(100)
# a = np.random.uniform(1,50, 20)
# lookfor a dedicated ufunc


# In[24]:


np.random.seed(100)
a = np.random.uniform(1,50, 20)

# Solution 1: Using np.clip
np.clip(a, a_min=10, a_max=30)


# In[ ]:


# Compute the min-by-max for each row for given 2d numpy array.
# each row - copute min/max. use apply_along_axis function

# np.random.seed(100)
# a = np.random.randint(1,10, [5,3])
# a
# #> array([[9, 9, 4],
# #>        [8, 8, 1],
# #>        [5, 3, 6],
# #>        [3, 3, 3],
# #>        [2, 1, 9]])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




