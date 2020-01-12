#name = input("enter your name")
#family = input("enter your family name")
#print("Welcome,", name,family)

# print(2/4-1)
# print(2//4-1)
# print((2+5)%3)
# print(3*4//6)
# print(3*2**2)
# print(3**2*2)
# print(-2**2)
# print(2**-2)
# print((-2)**2)
# print(-2**3**2)
# print((-2)**3**2)


# _length = (float)(input("enter _length"))
# _width = (float)(input("enter _width"))
# _area = _length * _width
# _pre = 2 * _length + 2 * _width
# print("_area,", _area)
# print("_pre,", _pre)

# num = (int)(input("enter num with 3 digits"))
# one = (num // 100)
# two = (num % 100) // 10
# three = (num % 10)
# print("one = ", one)
# print("two = ", two)
# print("three = ", three)
#
# sum = one + two + three
# print("sum = ", sum)

# import math as m
# a,b,c = (input("enter a")).split()
# print("a b c ", a,b,c)
# s = (int(a) + int(b) + int(c) ) / 2
# print(" s ", s)
# area = m.sqrt(s*(s-int(a))*(s-int(b))*(s-int(c)))
# print(" area ", area)

# pos_num = input("enter pos num")
# import math as m
# count = m.floor(m.log10(int(pos_num)) + 1)
# print (count)


# a,b = (input("enter a b")).split()
# a = int(a)
# b = int(b)
# xor = a and not b
# print(a and not b)

# s = 'seehemewe'
# print("s[-1:4:-1]" + s[-1:4:-1])
# print("s[-1:4]" + s[-1:4])
# print("s[4:-1]" + s[4:-1])
# print("s[0:3]" + s[0:3])#see
# print("s[3:5]" + s[3:5])#he
# print("s[-4:-2]" + s[-4:-2])#me
# print("s[7:]" + s[7:])#we
# print("s[3:6]" + s[3:6])#hem
# print("s[-4:-7:-1]" + s[-4:-7:-1])#meh
# print("s[-2:-4:-1] + s[-5]" + s[-2:-4:-1] + s[-5])#wee


stru = input("enter str")
#b = stru[0:len(stru)]
#print(b)
#option 1: c = stru[-1:-len(stru)-1:-1]
#print(c)
#ans = (b == c)
ans = stru[::-1] #option 2
print(ans)

