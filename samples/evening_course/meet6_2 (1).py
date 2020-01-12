import numpy as np

mt = np.empty((3,3))
print(mt)

count = 0
i = 0
j = 0

for i in range(3):
    for j in range(3):
        mt[i,j] = count
        count = count + 1

print(mt)


arr = np.arange(10,49,1)
print(arr)

np_zero = np.zeros(10)
print(np_zero)

