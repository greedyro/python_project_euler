def is_palindrome(number):
    strNum = str(number)
    if len(strNum) % 2 == 0:
        half = int(len(strNum) / 2)
        # print(f"half: {half}")
        for i in range(0, half + 1):
            end = len(strNum) - 1 - i
            if strNum[i] != strNum[end]:
                return False
        return True
    else:
        half = int(len(strNum) / 2) - 1
        end = len(strNum) - 1
        for i in range(0, half + 1):
            end = len(strNum) - 1 - i
            if strNum[i] != strNum[end]:
                return False
        return True

largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_palindrome(product):
            largest = max(largest, product)
print(f"Largest polindrome: {largest}")