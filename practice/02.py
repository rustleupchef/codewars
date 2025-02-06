nums = []

while True:
    num = input()
    if num == "0":
        break
    nums.append(int(num))

odds = []

for num in nums:
    if num % 2 != 0:
        odds.append(num)

if len(odds) > 0:
    for odd in odds:
        print(f"{odd} is odd")
    print("FLASH FAILED")
else:
    print("FLASH FORWARD")