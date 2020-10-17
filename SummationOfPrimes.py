import math

def is_prime(number):
    if number == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(number)) + 1,1):
        if number % i == 0:
            return False
    return True

sum = 2
for i in range(1, 2000000, 2):
    if is_prime(i):
        sum += i
        # print(i)

print(f"Total Sum: {sum}")