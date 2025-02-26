nums = [int(num) for num in [input(), input(), input()]]
nums = list(set(nums))
leading = max(nums)
del nums[nums.index(leading)]

start = True
minimum = 1
while start:
    minimum *= 2
    if (round(minimum ** leading ** -1,6)) % 1 == 0:
        for num in nums:
            if round(minimum ** num ** -1,6) % 1 > 0:
                break;
        else:
            start = False
            print(minimum)
