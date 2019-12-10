# Import numpy as np and print the version number.
import numpy as np
print(np.__version__)

# Create a 1D array of numbers from 0 to 9
# #> array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr = np.arange(10)
arr

# Create a 3×3 numpy array of all True’s


np.full((3, 3), True, dtype=bool)
np.ones((3,3), dtype=bool)


# Extract all odd numbers from arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# #> array([1, 3, 5, 7, 9])

arr[arr % 2 == 1]

# Replace all odd numbers in arr with -1

# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

arr[arr % 2 == 1] = -1
arr


# Replace all odd numbers in arr with -1 without changing arr
# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#hint - where

arr = np.arange(10)
out = np.where(arr % 2 == 1, -1, arr)
print(arr)
out
# np.arange(10)
# #> array([ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# Desired Output:
# #> array([[0, 1, 2, 3, 4],
# #>        [5, 6, 7, 8, 9]])
arr = np.arange(10)
arr.reshape(2, -1)  # Setting to -1 automatically decides the number of cols

# Stack arrays a and b vertically
# a = np.arange(10).reshape(2,-1)
# b = np.repeat(1, 10).reshape(2,-1)

a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.vstack([a, b])

# Get the common items between a and b
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# Desired Output:

# array([2, 4])


a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

# Get the positions where elements of a and b match
# a = np.array([1,2,3,2,3,4,3,4,5,6])
# b = np.array([7,2,10,2,7,4,9,4,9,8])
# Desired Output:

# #> (array([1, 3, 5, 7]),)

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

np.where(a == b)

# Get all items between 5 and 10 from a.
# a = np.array([2, 6, 1, 9, 10, 3, 27])
# Desired Output:

# (array([6, 9, 10]),)

a = np.array([2, 6, 1, 9, 10, 3, 27])

index = np.where((a >= 5) & (a <= 10))
a[index]

a[(a >= 5) & (a <= 10)]


# Reverse the rows of a 2D array arr.
# # Input
# arr = np.arange(9).reshape(3,3)

# Input
arr = np.arange(9).reshape(3,3)

arr[::-1]


# Reverse the columns of a 2D array arr. (last arr)


arr[:, ::-1]


# Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.



rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))
rand_arr

# Print or show only 3 decimal places of the numpy array rand_arr.
# hint: set_printoptions


np.set_printoptions(precision=3)
rand_arr = np.random.random([5,3])
rand_arr


# Limit the number of items printed in python numpy array a to a maximum of 6 elements.


# In[47]:


np.set_printoptions(threshold=6)
a = np.arange(15)
a


# In[ ]:





# In[50]:


# From the array a, replace all values greater than 30 to 30 and less than 10 to 10.
# np.random.seed(100)
# a = np.random.uniform(1,50, 20)
# lookfor a dedicated ufunc


# In[51]:


# Input
np.set_printoptions(precision=2)
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


# In[56]:


# Input
np.random.seed(100)
a = np.random.randint(1,10, [5,3])
a

np.apply_along_axis(lambda x: np.min(x)/np.max(x), arr=a, axis=1)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




