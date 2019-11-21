'''
def sum_mul(*args,initial_sum = 0,initial_product = 1,**keywd):
    print(args)
    print(initial_sum)
    print(initial_product)
    print(keywd)

    keys = (keywd.keys())
    for kw in keys:
        print (kw)
    print(keywd.get('tomer'))

'''
#*********************************
#sum_mul(1,2,3)

# dic1 = {1:"efes",
#         2:"one",
#         '2':"two"
#         }

# def t1(dic1):
#     print(dic1[1])
#     print(dic1['2'])

# t1(dic1)

#sum_mul(1,2,3,initial_sum = 5,initial_product=22, tomer =1, meital =2)
#sum_mul(1,2,3,initial_sum = 5,initial_product=22, **dic1)
#*********************************

# def get_anagrams(words):

#     n = [sorted(w) for w in words]
#     print(n)
#     normalized = ['**'.join(sorted(w)) for w in words]
#     print(normalized)

# print (get_anagrams(["pool", "loco", "cool", "stain", "satin", "pretty", "nice", "loop"]))


# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# new_a = [i for i in a if i %2 == 0]
# print(new_a)

def fibonacci():
    num = int(input("How many numbers that generates?:"))
    i = 1
    if num == 0:
        fib = []
    elif num == 1:
        fib = [1]
    elif num == 2:
        fib = [1,1]
    elif num > 2:
        fib = [1,1]
        while i < (num - 1):
            fib.append(fib[i] + fib[i-1])
            i += 1
    return fib
print(fibonacci())