import math
def fct():
    for a in range(1000):
        for b in range(a, 1000 - a):
            for c in range(b, 1000 - b):
                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print(f"a: {a}  b: {b}   c: {c}")
                        return a * b * c
    print("Exited fct without result")

print(fct())

# a: 200  b: 375   c: 425
# 31875000