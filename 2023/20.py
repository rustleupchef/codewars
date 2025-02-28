base = int(input())
exponent = int(input())
units = [base % 10, pow(base, 2) % 10]
i = 3
while units[-1] != units[0]:
    units.append(pow(base, i) % 10)
    i += 1
units.pop()
print(units)
print(units[(exponent - 1) % len(units)])
