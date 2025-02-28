num = input()
if num[-1] == '7':
    print(float(num) + 0.02)
elif float(num[-1]) % 2 == 1:
    print(float(num) - 0.09)
elif float(num[-1]) > 7:
    print(float(num) - 4.0)
elif float(num[-1]) < 4:
    print(float(num) + 6.78)