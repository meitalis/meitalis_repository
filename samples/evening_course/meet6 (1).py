# def concat_codons(codons,index):
#     thislist = []
#     for x in range(index, codons.__len__(), 3):
#         print(x)
#         tmp = codons[x:x + 3]
#         if len(tmp) == 3:
#             thislist.append(codons[x:x + 3])
#     return  thislist
#
# def concat_codons_short(codons,index):
#     return [codons[x:x + 3] for x in range(index, codons.__len__(), 3)  if len(codons[x:x + 3]) == 3]
#
#
# print(concat_codons_short("AGTCTTATATCT",1))

#
#
# def f1(a,b): print(a,b)
# def f2(a,*b): print(a,b)
# def f3(a,**b): print(a,b)
# def f4(a,*b,**c): print(a,b,c)
# def f5(a,b=2,c=3): print(a,b,c)
# def f6(a,b=2,*c): print(a,b,c)
#
#
# '''1 2 '''
# f1(1,2)
#
# '''1 2 '''
# f1(b=2,a=1)
#
# '''1 [2 3]'''
# f2(1,2,3)
#
# ''' 1{'x': 2, 'y': 3} '''
# f3(1,x = 2,y = 3)
#
# ''' 1 (2, 3) {'x': 2, 'y': 3 '''
# f4(1,2,3,x = 2,y = 3)
#
# ''' 1 2 3 '''
# f5(1)
#
# ''' 1 4 3'''
# f5(1,4)
#
# ''' 1 2 () '''
# f6(1)
#
# ''' 1 3 (4,) '''
# f6(1,3,4)
#


