nums = [int(num) for num in input().split()]
PTS = nums[0]
FGA = nums[1]
FTA = nums[2]
print(f"{round(100 * PTS/(2 * (FGA + (0.44 * FTA))),2)}%")