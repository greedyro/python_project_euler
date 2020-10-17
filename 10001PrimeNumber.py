import math

prime_count = 0
check_this_number = 1

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

while prime_count < 10001:
    # print(f"Checking prime count: {prime_count}")
    if is_prime(check_this_number):
        prime_count += 1
    check_this_number += 2

print(f"The 10001st Prime is {check_this_number - 2}")