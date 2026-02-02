#Problem 2 solution
def main():
    nums = input().split()
    x = int(nums[0])
    y = int(nums[1])
    print(int(x / y * (2 * y)))

if __name__ == "__main__":
    main()