def is_polyndrom(str):
    print(str)
    if len(str)==1:
        return True

    if len(str)==2:
        b = str[0]==str[-1]
    else:
        b = is_polyndrom(str[1:len(str) - 1])

    return str[0]==str[-1] and b


print("is poly ",is_polyndrom("redtder"))