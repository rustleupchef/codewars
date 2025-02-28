def mc_carthy(number):
    if (number > ZZ):
        return (number - XX)
    else:
        return mc_carthy(mc_carthy(number+YY))

nums = [int(num) for num in input().split(',')]
XX, YY, ZZ = nums[0], nums[1], nums[2]
num = int(input())
print(mc_carthy(num))