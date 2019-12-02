import math
import time


def is_prime(n):

    # 1 is not prime
    if n == 1:
        return False

    # 2 is prime
    if n == 2:
        return True

    # Even numbers are not prime
    if n % 2 == 0:
        return False

    max_devisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_devisor, 2):
        if n % d == 0:
            return False
    return True


# Test function
t0 = time.time()
count = 0

for n in range(300000000, 300500000):

    if is_prime(n):
        count += 1
        print(n, "is prime")

t1 = time.time()

print("Number of primes:", count)
print("Time required:", t1 - t0)

