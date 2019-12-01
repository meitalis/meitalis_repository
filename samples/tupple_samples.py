def publishError(startStr, endStr, *args):
    print(startStr)
    for elem in args :
        (x,y) = elem
    print(endStr)

publishError("[Start]" , "[End]" , ("Hello", "Hi") ,("Hello2", "Hi2"))