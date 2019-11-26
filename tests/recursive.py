# sample 4 - Write a Python program of recursion list sum.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21

def list_sum(num_List):
    print("num_List=",num_List)
    if len(num_List) == 1:
        return num_List[0]
    else:
        if type(num_List[0]) is list:
            return list_sum(num_List[0]) + list_sum(num_List[1:])
        else:
            return num_List[0] + list_sum(num_List[1:])

print(list_sum([1, 2, [3,4], [5,6]]))

# sample 3 - Write a Python program to converting an Integer to a string in any base

# def to_string(n,base):
#    conver_tString = "0123456789ABCDEF"
#    if n < base:
#       return conver_tString[n]
#    else:
#       print(n)
#       print(n//base)
#       print(n % base)
#       return to_string(n//base,base) + conver_tString[n % base]
#
# print(to_string(283,10))



# sample 2 - Write a Python program to calculate the sum of a list of numbers
# numbers = [7,6,2,1,1]
#
# def sum_list(i):
#     if i == len(numbers) - 1 :
#        return numbers[i]
#     else:
#        return numbers[i] + sum_list(i + 1)
#
# print(sum_list(0))
#
#
# def list_sum(num_List):
#     if len(num_List) == 1:
#         return num_List[0]
#     else:
#         return num_List[0] + list_sum(num_List[1:])
#
# print(list_sum([2, 4, 5, 6, 7]))


# sample 1
# def factorial_recursive(n):
#     # Base case: 1! = 1
#     if n == 1:
#         return 1

#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial_recursive(n-1)

# print(factorial_recursive(3))