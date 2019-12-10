import numpy as np


A = np.array([[1,3,4],[2,3,5],[0,1,-1]])
B = np.array([-1,1,-1])
C = np.array([[10,20,30],[0,1,0],[50,20,1]])
arr = np.array([[0, 7, 2],[ 3, 7, 7],[ 6, 7, 8]])
print(arr)
print(arr.flatten())
out = np.where(arr ==7)
print(len(out[0]))

#A*A
print(A@A)
print(A@A@A)
# [[ 1  4  9]
#  [16 25 36]]
# print(A**2)
# [[ 1  4  9]
#  [16 25 36]]
# print(A@A) #will not run 2*3 @ 2*3
# print(A*B)
# [[-1  2 -3]
#  [-4  5 -6]]
# print(C*C)
# [[ 100  400  900]
#  [   0    1    0]
#  [2500  400    1]]
# print(C@C)
# [[1600  820  330]
#  [   0    1    0]
#  [ 550 1040 1501]]

[

]

