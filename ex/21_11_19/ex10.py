def xor(a,b):
    ans = (a and not b) or (b and not a)
    print(ans)


def fand(a,b):
    ans = a and b
    print(ans)

def forf(a,b):
    ans = a or b
    print(ans)

xor(False,False)
xor(False,True)
xor(True,False)
xor(True,True)
print("********** and *********")
fand(False,False)
fand(False,True)
fand(True,False)
fand(True,True)

print("********* or **********")
forf(False,False)
forf(False,True)
forf(True,False)
forf(True,True)

