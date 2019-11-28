disks = 3
A = 'A'
C = 'C'
B = 'B'

def hanoi(n, A, C, B):
    print('n', n, A, C, B)
    if n > 0:
        hanoi(n-1, A, B, C)
        print ('n',n,'move disk from ', A, ' to ', C)
        hanoi(n-1, B, C, A)
    else:
        print('n',n,"do nothing")

hanoi(disks, A, C, B)


# disks = 5
# from_tower = 'A'
# to_tower = 'C'
# using_tower = 'B'
#
# def hanoi(n, from_tower, to_tower, using_tower):
#     if n > 0:
#         hanoi(n-1, from_tower, using_tower, to_tower)
#         print ('n',n,'move disk from ', from_tower, ' to ', to_tower)
#         hanoi(n-1, using_tower, to_tower, from_tower)
#     else:
#         print('n',n,"do nothing")
#
# hanoi(disks, from_tower, to_tower, using_tower)

#
#
# def hanoi (n,stick_src,stick_middle,stick_dst):
#     #print("n=",n,"stick_src= ", stick_src, "stick_middle= ", stick_middle, "stick_dst= ", stick_dst)
#     if n == 1:
#         return
#
#     hanoi(n-1,stick_src,stick_dst,stick_middle)
#     if stick_src:
#         stick_dst.append(stick_src.pop())
#     print("n=", n, "stick_src= ", stick_src, "stick_middle= ", stick_middle, "stick_dst= ", stick_dst)
#     hanoi(n - 1, stick_middle, stick_src, stick_dst)
#
#
#
# def run ():
#     stick_src = [5,4,3,2,1]
#     stick_middle = []
#     stick_dst = []
#     hanoi(len(stick_src)+1,stick_src,stick_middle,stick_dst)
#     print("stick_src= " , stick_src,"stick_middle= ",stick_middle,"stick_dst= " , stick_dst)
#
# run()