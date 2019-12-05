


# import numpy as np
# year = np.array([1900,1904,1990,1993,2000,2014,2016,2100])
# lyear = year[year%4==0]
# print(lyear)

#########################

# import numpy as np
# a = np.arange(1,49).reshape(3,4,4)
# print("a",a)
# slice1 = a[0,2,:]
# slice1
# print("\n")
# print("slice1\n",slice1)
#
# slice2 = a[2]
# print("\n")
# print("slice2\n",slice2)
#
# slice3 = a[:,1:2,0:2]
# print("\n")
# print("slice3\n",slice3)
#
# slice4 = a[2,:,-1:-3:-1]
# print("\n")
# print("slice4\n",slice4)
#
# slice5 = a[:,-1::-1,0:1]
# #slice5 = a[:,-1::-1,0]
#
# print("\n")
# print("slice5\n",slice5)


#########################

# import numpy as np
# a = np.ones((3, 3))
# a
# b = np.array([2,2,2])
# c = np.vstack((a,b))
# c
# d = np.array([3,3,3,3])
# e = np.column_stack((c,3*np.ones(4)))
# e

#########################

# import numpy as np
# a = np.array([[10,11,12,13],[21,22,23,24]])
# a
# b = a.flatten()
# b
# c = a.ravel()
# c
# c[0] = 50
# print('a',a)
# print('c',c)
# a.resize(1,4)
# a.resize(1,4,refcheck = False)

#########################

# import numpy as np
# np.array([1, 2, 3, 4])
# np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
# np.zeros((3, 2))
# a = [1, 2, 3, 4]
# np.ones_like(a)
# np. * np.zeros(3)
# np.nan * np.zeros(3)
# np.array([[1, 2, 3], np.ones(3)])
# np.linspace(0, 1000, 6)
#
# #########################
# # Create a 3 × 3 matrix with values ranging from 0 to 8
# Create
# a
# Hilbert
# matrix
# of
# size
# N × N(N is given
# by
# the
# user))
# np.array(range(9))
# a.shape = (3, 3)
# a

# # Create an array with values ranging from 10 to 49
# np.array(range(10, 50))

# # Create a vector of size 10 containing only zeros of integer type
# v = np.zeros(10, dtype=int)
# v

# # Create a Hilbert matrix of size N × N (N is given by the user)
# import numpy as np
# mt = np.zeros((5,5))
# #print(mt)
#
# i = 1
# j = 1
#
# for i in range(0,5):
#     for j in range(0,5):
#         mt[i,j] = i + 1 +j + 1 -1
#
# mt = 1/mt
# print(mt)


# import numpy as np
#
# n = 3
# matrix = np.zeros([n, n])
# x = 0
# y = 1
#
#print(-2%3)
#print(2%3)
# matrix[x, y] = 1
# for i in range(2, 10):
#     xt, yt, x, y = x, y, (x - 1) % n, (y + 1) % n
#
# if matrix[x, y] != 0:
#     x = (xt + 1) % n
# y = yt
#
# print(i, "x", x, "y", y)
# matrix[x, y] = i
# matrix



# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([[1, 0], [0, 1]])
# print(b)


# a = np.array([[1, 2], [3, 4]])
# print(a)
# b = np.array([[1, 0], [0, 1]])
# print(b)



# a = np.array([[1, 2], [3, 4]])
# # print(a)
# b = np.array([[1, 0], [0, 1]])
# # print(b)


# a * b
# # c = a@b
# # j = a.dot(b)
# # print("j",j)



# a = np.array([[1, 2, 3, 4]])
# a.resize((2, 2))
# a

#
# b = np.array([[1, 2], [3, 4]])
# b.flatten()
#


# c = np.array([[1, 2], [3, 4]])
# c.ravel()
#
#
