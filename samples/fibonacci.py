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
# ***********************************************************
# def fibonacci():
#     num = int(input("How many numbers that generates?:"))
#     i = 1
#     if num == 0:
#         fib = []
#     elif num == 1:
#         fib = [1]
#     elif num == 2:
#         fib = [1,1]
#     elif num > 2:
#         fib = [1,1]
#         while i < (num - 1):
#             fib.append(fib[i] + fib[i-1])
#             i += 1
#     return fib
# print(fibonacci())