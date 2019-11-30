
def is_prime(number):

    return True if 0 not in [number % j for j in range(2, number)] else False
    # return [i for i in range(2,number+1) if 0 not in [i%j for j in range(2,i)]]

print(is_prime(42))
print(is_prime(43))