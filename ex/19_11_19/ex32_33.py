#ex 32
'''
a = ['A','B','C','D','E','F','G']
b = [4,  2,   6,  1,  5,  0,  3]

ans = [a[x] for x in b]
print(ans)

ans = [a[x] for x in sorted(b)]
print(ans)

ans = [a[b[x]] for x in b]
print(ans)

ans = list(zip(b,a))
print(ans)

ans = sorted(zip(b,a))
print(ans)


ans = [x for (y,x) in sorted(zip(b,a))]
print(ans)
'''


#ex 32


#ex.33
'''
nmax = 5
x = [1]

for n in range(1 , nmax +2):
    print(x)
    x = [([0] + x)[i] + (x + [0] ) [i] for i in range(n +1)]
'''
#ex.33

