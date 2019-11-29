def func1(numbers,target,num_slice = [],sum_slice = 0):
    #print(numbers,target,num_slice,sum_slice)
    if sum_slice == target:
        yield num_slice

    if sum_slice > target:
        return

    for i in range(len(numbers)):

        n = numbers[i]
        #print("n", n,"i",i)
        yield from func1(numbers[i+1:],target,num_slice + [n],sum_slice + n)



g = func1([7, 4, 1, 2, 6, 1],8)
for i in g:
    print(i)






# #7 6 4 2 1 1 /8

# numbers = [7, 6, 4, 2, 1, 1]
# S = 8
# answers = []
#
# def func1(numbers,target,num_slice = []):
#     s = sum(num_slice)
#     print("*** s", s,"num_slice",num_slice,"numbers",numbers)
#
#     if s > target:
#         return
#     if s == target:
#         print("sol",num_slice)
#
#     for i in range(len(numbers)):
#         n = numbers[i]
#         print("i",i,"n", n)
#         func1(numbers[i+1:],target,num_slice + [n])
#
#
#
# func1( [7, 4, 1, 2, 6, 1],S)

# def subset_sum(numbers, target, partial=[], partial_sum=0):
#     if partial_sum == target:
#         yield partial
#     if partial_sum >= target:
#         return
#     for i, n in enumerate(numbers):
#         remaining = numbers[i + 1:]
#         yield from subset_sum(remaining, target, partial + [n], partial_sum + n)
#
# for i in subset_sum([7, 4, 1, 2, 6, 1],8):
#     print(i)
############################################

############################################

# def subset_sum(numbers, target, partial=[]):
#     s = sum(partial)
#
#     # check if the partial sum is equals to target
#     if s == target:
#         print (partial, target)
#     if s >= target:
#         return  # if we reach the number why bother to continue
#
#     for i in range(len(numbers)):
#         n = numbers[i]
#         remaining = numbers[i+1:]
#         subset_sum(remaining, target, partial + [n])
#
#
#
# subset_sum([3,9,8,4,5,7,10],15)


     #Outputs:
    #sum([3, 8, 4])=15
    #sum([3, 5, 7])=15
    #sum([8, 7])=15
    #sum([5, 10])=15


    # def subset_sum(numbers, target, partial=[], partial_sum=0):
    # if partial_sum == target:
    #     yield partial
    # if partial_sum >= target:
    #     return
    # for i, n in enumerate(numbers):
    #     remaining = numbers[i + 1:]
    #     yield from subset_sum(remaining, target, partial + [n], partial_sum + n)


        # def sum_digits(number):
#     """ Return the sum of digits of a number.
#         number: non-negative integer
#     """

#     # Base Case
#     if number == 0:
#         return 0
#     else:
#         # Mod (%) by 10 gives you the rightmost digit (227 % 10 == 7),
#         # while doing integer division by 10 removes the rightmost
#         # digit (227 // 10 is 22)

#         return (number % 10) + sum_digits(number // 10)


# print(sum_digits(565656))
