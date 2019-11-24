def triangular_numbers(n):
    t = 0
    for i in range(1,n):
        yield t
        t = t + i


print(list(triangular_numbers(10)))


print(list(i*(i+1)//2 for i in range(1,10)))


