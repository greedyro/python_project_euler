import math

def factor(number):
    count = 2
    if number == 1:
        count = 1
    elif number == 3:
        count = 2
    elif number == 6:
        count = 4
    elif number % 2 == 0:
        count += 2
    elif number % 3 == 0:
        count += 2

    # count = 1
    for i in range(4, int(math.sqrt(number) + 1)):
        if number % i == 0:
            count += 2
    # print(f"Checking: {number}   Answer: {count}")
    return count

found = False
j = 1
p = 1
while not found:
    if factor(j) > 500:
        found = True
    else:
        p += 1
        j += p



print(f"We found it {j}")

# 76576500 correct