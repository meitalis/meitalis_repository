import math

a = 4.503# input("enter a")
b = 2.377#input("enter b")
c = 3.902#input("enter c")
S = 0.5 * (float(a) + float(b) + float(c))
A = math.sqrt(S * (S-a) * (S-b) * (S-c))

print(A)

#enter a4.503
#enter b2.377
#enter c3.902

#ans 4.635