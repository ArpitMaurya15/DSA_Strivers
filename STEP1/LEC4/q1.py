num = 12
n = abs(num)
count = 0

if n == 0:
    count = 1
else:
    while n > 0:
        n = n // 10
        count += 1

print("Total digits:", count)
