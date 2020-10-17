count_and_num = (1, 1)  # count, number
for i in range(1000000, 1, -1):
    # print(i)
    count = 0
    num = i
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = 3 * num + 1
        count += 1

    if count_and_num[0] < count:
        count_and_num = (count, i)

print(f"Answer: {count_and_num}")

# 837799
