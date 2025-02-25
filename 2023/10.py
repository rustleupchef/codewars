def is_Prime(n: int) -> bool:
    if n <= 1: return False

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

text = input()

n1, n2 = text.split(";")[0], text.split(";")[1]
n1, n2 = int(n1), int(n2)

count = 0
result = 0
i = n2 + 1

while count < n1:
    if not is_Prime(i):
        if count == 0:
            result = i
        count += 1
    else:
        count = 0
    i += 1

print(result)