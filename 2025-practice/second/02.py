even = list()
odd = list()

while True:
    num = int(input())
    if num == 0:
        break
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

if len(even) > len(odd) and len(odd) > 0:
    print(f"{odd[0]} is not even")
elif len(odd) > len(even) and len(even) > 0:
    print(f"{even[0]} is not odd")
else:
    print("NO LIST PROBLEMS FOUND")