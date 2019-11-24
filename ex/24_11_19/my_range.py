def my_range(start,stop,step = 1):
    current = start
    while current < stop:
        yield current
        current += step

for n in my_range(-1,100,5):
    print(n,end=' ')

# print(range(-3))
# for i in range(-3):
#     print (i)
#     