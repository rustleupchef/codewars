times = int(input())

lines = []

for i in range(times):
    lines.append(input())

lines.reverse()

for line in lines:
    print(line)