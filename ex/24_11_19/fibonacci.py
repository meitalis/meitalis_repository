from random import randint

def fib(n):
    a,b = 0,1
    for i in range(n):
        yield a
        print("before a",a,"b", b)
        a,b = b,a+b
        print("after a", a, "b", b)

for a in fib(10):
    print (a)

print(list(fib(10)))

