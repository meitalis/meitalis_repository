import numpy as np
# Create a 4X2 integer array and Prints its attributes
# Expected Output:

# Printing Array

# [[64392 31655]
#  [32579     0]
#  [49248   462]
#  [    0     0]]

# Printing numpy array Attributes

# 1> Array Shape is:  (4, 2)
# 2>. Array dimensions are  2
# 3>. Length of each element of array in bytes is  2

#
# import numpy as np
# #a = np.arange(1,9,dtype=np.short).reshape(4,2)
# #a = np.array([[64392,31655],[32579,0],[49248,462],[0,0]],dtype=np.int)
# a = np.random.randint(1,100000,(4,2))
# print(a)
# print("shape",a.shape)
# print("dimensions",a.ndim)
# #print("Length of each element of array in bytes is",np.dtype(np.int).itemsize)
# print("Length of each element of array in bytes is",a.itemsize)

# *************************************************************************************#
# Create a 5X2 integer array from a range between 100 to 200 such that the difference between
# each element is 10
# Expected Output:

# Creating 5X2 array using numpy.arange
# [[100 110]
#  [120 130]
#  [140 150]
#  [160 170]
#  [180 190]]


# a = np.arange(100,200,step=10).reshape(5,2)
# a

# *************************************************************************************
# Following is the given numpy array return array of odd rows and even columns
# import numpy

# sampleArray = numpy.array([[3 ,6, 9, 12], [15 ,18, 21, 24], 
# [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])

# Expected Output:

# Printing Input Array
# [[ 3  6  9 12]
#  [15 18 21 24]
#  [27 30 33 36]
#  [39 42 45 48]
#  [51 54 57 60]]

#  Printing array of odd rows and even columns
# [[ 6 12]
#  [30 36]
#  [54 60]]


# sampleArray = np.array([[3 ,6, 9, 12], [15 ,18, 21, 24], [27 ,30, 33, 36], [39 ,42, 45, 48], [51 ,54, 57, 60]])
# print(sampleArray)
#
# print(sampleArray[0::2,1::2])

# *************************************************************************************

# ____Split____ the array into four equal-sized sub-arrays
# Note: Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 
# and then Split the array into four equal-sized sub-arrays.

# Expected Output:

# Creating 8X3 array using numpy.arange
# [[10 11 12]
#  [13 14 15]
#  [16 17 18]
#  [19 20 21]
#  [22 23 24]
#  [25 26 27]
#  [28 29 30]
#  [31 32 33]]

# Dividing 8X3 array into 4 sub array

# [array([[10, 11, 12],[13, 14, 15]]), 
# array([[16, 17, 18],[19, 20, 21]]), 
# array([[22, 23, 24],[25, 26, 27]]), 
# array([[28, 29, 30],[31, 32, 33]])]

#
# a = np.arange(10,34,step=1).reshape(8,3)
# print(a)
# b = a.reshape(4,2,3)
# print(b)
# *************************************************************************************

# Sort following NumPy array
# 7.1- by the second row and
# 7.2-by the second column
# import numpy
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]])
# Expected Output:

# Printing Original array
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]

# Sorting Original array by secoond row
# [[73 43 34]
#  [12 22 82]
#  [66 94 53]]

# Sorting Original array by secoond column
# [[82 22 12]
#  [34 43 73]
#  [53 94 66]]


#
# sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
# print("** sampleArray ****")
# print(sampleArray)
# b = np.argsort(sampleArray[1,:])
# print("** b ****")
# print(b)
# c = sampleArray[:,b]
# print("** c ****")
# print(c)
# print("** sampleArray ****")
# print(sampleArray)
# d = np.argsort(sampleArray[:,1])
# print("** d ****")
# print(d)
# e = sampleArray[d,:]
# print("** e ****")
# print(e)

# *************************************************************************************



# Following is the input NumPy array ____delete____ column two and ____insert____ following new column in its place.
# import numpy
# sampleArray = numpy.array([[34,43,73],[82,22,12],[53,94,66]]) 

# newColumn = numpy.array([[10,10,10]])
# Expected Output:

# Printing Original array
# [[34 43 73]
#  [82 22 12]
#  [53 94 66]]

# Array after deleting column 2 on axis 1

# [[34 73]
#  [82 12]
#  [53 66]]
# Array after inserting column 2 on axis 1

# [[34 10 73]
#  [82 10 12]
#  [53 10 66]]


sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)
a = np.delete(sampleArray,1,axis=1)
print(a)
newColumn = np.array([[10,10,10]])
b = np.insert(a,1,newColumn,axis=1)
print(b)















