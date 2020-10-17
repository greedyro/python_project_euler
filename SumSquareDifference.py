import math
sum = 0
sumSqr = 0
for i in range(1,101):
    sum += i**2
    sumSqr += i

sumSqr = sumSqr**2
print(f"Difference of sums is: {sumSqr - sum}")