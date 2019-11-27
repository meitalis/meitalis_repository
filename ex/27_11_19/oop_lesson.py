#sample 2
# def add_third(f):
#     return lambda *args: 2 + f(*args)
# def add_third(f):
#     def internal_func(*args):
#         return 1 + f(*args)
#     return internal_func
#
# @add_third
# def add_two(a,b):
#     return a + b
#
# print(add_two(3,4))

#sample 1
# def five_time(func,*args):
#     def internal_func(*args):
#         return 5 * func(*args)
#     return internal_func
#
# #no decorate return 8 with decorate return 40
# @five_time
# def sum_nums(a,b):
#     return a+b
#
# print(sum_nums(3,5))