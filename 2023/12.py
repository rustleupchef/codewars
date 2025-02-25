nums = input().split(";")
goal = int(nums[-1])
nums = nums[:-1]

def test(nums: list[str], target: int) -> bool:
    temp = 0
    for num in nums: 
        temp += int(num)
    return temp == target

if test(nums, goal):
    print("No broken numbers")
else:
    for i in range(10):
        temp = nums[:]
        temp = [num.replace(f"{i}", "") for num in nums]
        if test(temp, goal): 
            print(i)
