def is_polyndrom(str):
    print(str)
    if len(str)==1:
        return True

    if len(str)==2:
        return str[0]==str[-1]

    return is_polyndrom(str[1:len(str) - 1])

print("is poly ",is_polyndrom("redtader"))