num = int(input())
i = 0
while True:
    reverse = str(num)
    if len(reverse) != 4:
        print("INVALID NUMBER")
        break
    if i % 2 == 0:
        reverse = reverse[0] + reverse[1:3][::-1] + reverse[3]
    else:
        reverse = reverse[:2][::-1] + reverse[2:][::-1]
    num = abs(int(reverse) - int(reverse[::-1]))
    if num == 6174:
        print(i + 1)
        break
    i += 1
