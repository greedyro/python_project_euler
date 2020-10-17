fib1 = 1
fib2 = 2
fib3 = 0
sum = 2
while True:
    fib3 = fib1 + fib2
    if fib3 >= 4000000:
        break
    if fib3 % 2 == 0:
        sum += fib3
    fib1 = fib2
    fib2 = fib3

print(f"Sum: {sum}")