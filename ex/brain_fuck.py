def incrementPointer(code,sentence,c_position,s_position,parenthesis):
    #print("incrementPointer")
    return (c_position,s_position + 1)


def decrementPointer(code,sentence,c_position,s_position,parenthesis):
    #print("decrementPointer")
    return (c_position,s_position - 1)

def increment(code,sentence,c_position,s_position,parenthesis):
    #print("increment")
    sentence[s_position] += 1
    return (c_position,s_position)

def decrement(code,sentence,c_position,s_position,parenthesis):
    #print("decrement")
    sentence[s_position] -= 1
    return (c_position,s_position)

def output(code,sentence,c_position,s_position,parenthesis):
    #print("output ")
    print(chr(sentence[s_position]),end = "")
    return (c_position,s_position)

def accept(code,sentence,c_position,s_position,parenthesis):
    #print("accept")
    sentence[s_position] = input("set char")
    return (c_position,s_position)

def jump_forward(code,sentence,c_position,s_position,parenthesis):
    #print("jump_forward")
    #print(parenthesis)
    if sentence[s_position] == 0:
        i = code.index(']')
        print (i)
        return ((i + 1),s_position)

    #print ("append parenthesis ",c_position)
    parenthesis.append(c_position)
    return (c_position,s_position)


def jump_back(code,sentence,c_position,s_position,parenthesis):
    #print("jump_back",c_position,code)
    #print ("s_position=",s_position,sentence[s_position])
    #print(parenthesis)

    position = parenthesis.pop()
    #print ("pop parenthesis  ", position)
    if sentence[s_position] == 0:
        return ((c_position),s_position)

    c_position = position #code.rfind('[',0,c_position) -1

    c_position -= 1
    return (c_position,s_position)

def run():
     #input("enter characters")


    #code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>." Hello Wo
    code = "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."
    #code = "++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>." Hello World
    c_position = 0

    parenthesis = []
    sentence = [0]*len(code)
    s_position = 0

    #dictionary
    switcher={
                '>':incrementPointer,
                '<':decrementPointer,
                '+':increment,
                '-':decrement,
                '.':output,
                ',':accept ,
                '[':jump_forward,
                ']':jump_back

            }

    print('******************** START **************************************')
    while c_position < len(code):
        #print("char in position ",c_position, code[c_position],"s pos =",s_position,end=" ")
        # print("sentence[5]",sentence[5],end=" ")
        #print(parenthesis)
        c_position, s_position = switcher.get(code[c_position], -1)(code,sentence,c_position,s_position,parenthesis)
        #print(parenthesis)
        #print("/ do function / c pos =",c_position,"s pos =",s_position," / ", sentence[0],sentence[1],sentence[2],sentence[3],sentence[4],sentence[5],end=" ")
        c_position += 1
        #print("/c pos =",c_position)


run()