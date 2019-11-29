def notCollide(N,qns,q):
    if (q in qns):
        return False
    for key in qns.keys():
        if (key[0] == q[0] or
            key[1] == q[1] or
            abs(key[0] - q[0]) == abs(key[1] - q[1])):
                return False
    return True


def Nqueens(N,row = 0, qns = {}):
    num_sols = 0
    if (len(qns) - N == 0):
        return 1
    for i in range(N):
        if (notCollide(N,qns,(row,i))):
            qns[(row,i)] = 1
            num_sols += Nqueens(N,row+1,qns)
            qns.pop((row,i))
    return num_sols


if (__name__== '__main__'):
    print([Nqueens(i) for i in range(1,11)])

