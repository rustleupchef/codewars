nums = [int(num) for num in input().split(',')]
dices, faces = nums[0], nums[1]
nums = [int(num) for num in input().split(',')]
for num in nums:
    num += -2 if num % 2 == 0 else 3
    num %= faces
    if num == 0: num = faces
    print(num, end=" ")
