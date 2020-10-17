import math

given_number = 600851475143
small_number = 13195


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


for i in range(math.ceil(math.sqrt(given_number)), 2, -1):
    if given_number % i == 0:
        if is_prime(i):
            print(f"Largest Prime: {i}")
            break
print(f"Finished")