
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
#
def is_power_of_5(n):
    while n % 5 == 0 and n > 0:
        n = n // 5
    return n == 1
#
def is_power_of_2(n):
    while n % 2 == 0 and n > 0:
        n = n // 2
    return n == 1
#
def is_power_of_2(n):
    while n % 2 == 0 and n > 0:
        n = n // 2
    return n == 1

