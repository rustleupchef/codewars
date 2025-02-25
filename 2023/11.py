num = int(input())
i = 1

while True:
    if (num + i) % (i + 1) > 0:
        break
    i += 1

print(num + i)