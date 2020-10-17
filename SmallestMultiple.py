# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


num = 2

while True:
    found = True
    for i in range(1, 21):
        if num % i != 0:
            found = False
            break
    if found:
        print(f"Smallest number: {num}")
        break
    num += 2
    # print(f"Number to check: {num}")

print("Finished")
# 232792560