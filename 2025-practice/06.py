quaternaries = []
while True:
    num = input()
    if num == "000":
        break
    quaternaries.append(int(num, 4))

for num in quaternaries:
    print(num)