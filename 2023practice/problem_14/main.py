#Problem 14 solution

def trib(num):
    if num == 0:
        return num
    if num < 3:
        return 1
    
    nums = [0, 1, 1]
    current = 0
    for i in range(3, num):
        current = sum(nums)
        nums.append(current)
        del nums[0]
    
    return sum(nums)


def main():
    nums = []
    while True:
        line = input()
        if line == "0 0":
            break
        nums.append([int(x) for x in line.split()])
    
    for parts in nums:
        print(trib(parts[0]) - trib(parts[1]))

if __name__ == "__main__":
    main()