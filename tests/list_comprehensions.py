'''
l1 = [(lambda x: x * 3)(x) for x in range(30)]
print(l1,end = '\n\n')

l2 = [(lambda i:'*' * i)(i) for i in range(10) if i > 0]
print(l2,end = '\n\n')

t1 = tuple(((lambda i:'*' * i)(i), i) for i in range(10) if i > 0)
print(t1,end = '\n\n')
'''
#########################################################
'''
def f(x):
    return x*3
l = [f(x) for x in range(20)]
print(l)
'''
#######################################################

# def diagonal(matrix):
#     m = [ [ ( matrix[i][j]) if i==j else 0 for j in range(len(matrix[i])) ] for i in range(len(matrix)) ]
#     return m

# matrix =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# d = diagonal (matrix)
# print(d)

#######################################################

# def sum2a(l,n):
#     for i in l:
#         diff = n - i
#         if diff in l:
#             return i,diff
#     else:
#         return None

# print(sum2a([3, -1, 6, 5, 9], 9))

def sum2b(l,n):
    a1 = set(l)
    a2 = {n - i for i in l}

    pairs = a1 & a2

    for i in pairs:
        if i != n/2:
            return i,n-i
    return None

print(sum2b([1, 6, 5,4,4, 9], 8))






