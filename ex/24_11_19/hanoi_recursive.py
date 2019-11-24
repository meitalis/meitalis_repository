def hanoi (n,stick_src,stick_middle,stick_dst):
    if n == 1:
        return

    hanoi(n-1,stick_src,stick_dst,stick_middle)
    if stick_src:
        stick_dst.append(stick_src.pop())
    hanoi(n - 1, stick_dst, stick_middle, stick_src)



def run ():
    stick_src = [5,4,3,2,1]
    stick_middle = []
    stick_dst = []
    hanoi(len(stick_src),stick_src,stick_middle,stick_dst)
    print("stick_src= " , stick_src,"stick_middle= ",stick_middle,"stick_dst= " , stick_dst)

run()