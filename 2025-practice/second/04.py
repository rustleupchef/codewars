nums = []
while True:
    num = input()
    if num == "0":
        break
    nums.append(int(num, 3))
for num in nums: print(num)