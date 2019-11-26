



# #7 6 4 2 1 1 /8

numbers = [7, 6, 4, 2, 1, 1]
S = 8
answers = []

def check(left,current):
    if (left + current) > S:
        return 0
    return left + current

def sum_by_num(n,num_slice):

    ans = check(n,num_slice[0])
    if (ans == S):
        print("found",n,num_slice[0])
        return
    else:
        ans = check(n,num_slice[0])


def all_sum():
    for n in range(len(numbers)):
        print("[all sum] n",n)
        if (n + 1) == len(numbers):
            break
        print("[all sum] numbers[n]",numbers[n],"numbers[n+1]",numbers[n+1])
        ans = check(numbers[n],numbers[n+1])
        print("[all sum] ans",ans)
        if ans == S:
            answers.append((numbers[n],numbers[n+1]))
        else:
            ans = check(numbers[n],numbers[n+2])

    print (answers)
all_sum()



def subset_sum(numbers, target, partial=[]):
    s = sum(partial)

    # check if the partial sum is equals to target
    if s == target:
        print (partial, target)
    if s >= target:
        return  # if we reach the number why bother to continue

    for i in range(len(numbers)):
        n = numbers[i]
        remaining = numbers[i+1:]
        subset_sum(remaining, target, partial + [n])



subset_sum([3,9,8,4,5,7,10],15)


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
