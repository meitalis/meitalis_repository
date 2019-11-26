try:
    num = int(input("enter num"))
    res = 10 / num
except (ZeroDivisionError):
    print ("ZeroDivisionError")
except ValueError:
    print ("ValueError")
except:
    print ("Default")


try:
    num = int(input("enter num"))
    res = 10 / num
except (ZeroDivisionError,ValueError):
    print ("ZeroDivisionError + ValueError")
except:
    print ("Default")
else:
    #executed if an exception was not raised
finally:
    #always executed,
