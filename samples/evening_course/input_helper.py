def get_int():
   while True:
        try:
            x = input("Please enter a integer:")
            n = int(x)
            if n < 0:
                print("is not positive" , n)
            return n
        except ValueError:
            print("is not positive" , x)

def get_positive_int():
    x = input("Please enter a positive integer:")

    while type(x) is not int:
        try:
            x = input("Please enter a positive integer: ")
            n = int(n)
            if n < 0:
                print("%d is not positive./n" % n)
            return n
        except ValueError:
            print("%s is not a positive integer.\n" % n)





