# Ex49::Write a Python program to find the index of the first term in the Fibonacci sequence to contain 500 digits
# sample: ...
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
# my solution
import itertools

def fib(digits):
    a,b = 0,1
    for i in itertools.count():
        l = len(str(a))
        if l == digits:
            return i
        a, b = b, a + b


print(fib(500))

# web solution
# import itertools
# def Fibonacci_sequence(n):
# 	DIGITS = n
# 	prev_num = 1
# 	cur_num = 0
# 	for i in itertools.count():
# 		# At this point, prev = fibonacci(i - 1) and cur = fibonacci(i)
# 		if len(str(cur_num)) > DIGITS:
# 			raise RuntimeError("Not found")
# 		elif len(str(cur_num)) == DIGITS:
# 			return str(i)
# 		prev_num, cur_num = cur_num, prev_num + cur_num

#print(Fibonacci_sequence(500))
