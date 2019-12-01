#1.5
# with open("Names.txt","r") as fp:
#     print(max(fp.readlines(),key=len))
#     print(sorted([(len(line.strip()),line) for cnt, line in enumerate(fp)])[-1][1])


# with open("Names.txt","r") as fp:
#     print(sum([(len(line.strip())) for line in fp]))


# with open("Names.txt","r") as fp:
#     lst = [(len(line.strip()),line.strip()) for line in fp]
#     min_v = (min(lst))
#     print('\n'.join(list(line[1] for line in lst if line[0] == min_v[0])))
#another option to solve with sorted: print(sorted(fp.readlines(), key=len))

# with open("Names.txt","r") as fr , open("name_length.txt","w") as fw:
#     fw.writelines([str(len(line.strip())) + '\n' for line in fr])

# with open("Names.txt","r") as fp:
#     length = input('Enter name length:')
#     print(''.join(list(line for line in fp if len(line.strip()) == int(length))))

#1.3.4
# password = "sljmai ugrf rfc ambc: lglc dmsp mlc rum"
# def decrypt():
#     return [chr(ord(char) + 2) if char != ' ' else char for char in password]
#     # lst = []
#     # for char in password:
#     #     lst.append(chr(ord(char) + 2))
#     # return lst
#
# print(' '.join(decrypt()))

#1.3.3
# def is_funny(string):
#     return False if False in list(map(lambda char: False if (char != 'h' and char != 'a') else True,string)) else True
#     # for char in string:
#     #     if char != 'h' and char != 'a':
#     #         return False
#     # return True
#
#
# print(is_funny("hahahahahkkaha"))
#True
#1.3.2
# def is_prime(number):
#
#     return True if 0 not in [number % j for j in range(2, number)] else False
#     # return [i for i in range(2,number+1) if 0 not in [i%j for j in range(2,i)]]
#
# print(is_prime(42))
# print(is_prime(43))

#ans
# False
# True

#1.3.1
# def intersection(list_1, list_2):
#     return {i for i in list_1 if i in list_2 }
#
# print(intersection([1, 2, 3, 4], [8, 3, 9]))
# print(intersection([5, 5, 6, 6, 7, 7], [1, 5, 9, 5, 6]))
#ans
# [3]
# [5,6]

#1.2.5
# import functools

# def function(num, item):
#     print(num,item)
#     return num + 1
#
# lst = list(map(int, '444'))
# magic = functools.reduce(function, lst)
# print(magic)
# result = (lambda x: x % 4 == 0)(magic)
# if result:
#     print("Correct password!")
# else:
#     print("Wrong password.")
#444 = 6
#2301 - 5
#1.2.1
# print(not 0 < 2)
# print((not 0) < 2)
# print(3 == True)
# print(bool(3) == True)
# print(1 and 2)
# print(0 and 1)
# print(1 or 0)
# a = lambda x: 1
# print(a(3))
# print(a("s"))
# print(a(2))
# print(type(a(3)))


#1.1.4
# import functools
# def f(x,y):
#     return int(x) + int(y)
#
# def sum_of_digits(number):
#     return functools.reduce(f,str(number))
#
# print(sum_of_digits(104))
#ans 5

#1.1.3
# def is4divide(n):
#     return n % 4 == 0
#
# def four_dividers(number):
#     return list(filter(is4divide,range(1,number)))
#print(four_dividers(9))
#print(four_dividers(3))

# 1.1.2
# def power_c(c):
#     return c * 2
#
# def double_letter(word):
#     return ''.join(map(power_c,list(word)))
#
# print(double_letter("python"))
# print(double_letter("we are the champions!"))


# def secret(a):
#     return a % 3 != 0 and a % 5 != 0
# result = filter(secret, range(1, 31))
# print(list(result))

# import functools
# def f(a, b):
#     if a < b:
#         return a
#     else:
#         return b
# print(functools.reduce(f, [47,11,42,102,13],15))
#
# def combine_coins(coin,numbers):
#     return ''.join(map(lambda x: str(x) + coin, numbers)) #0$1$2$3$4$
#     #return ''.join(map(lambda s,n:s + str(n),[coin for i in numbers] , numbers)) #$0$1$2$3$4
#
#
# print(combine_coins('$',[0,1,2,3,4]))