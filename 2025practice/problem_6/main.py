#Problem 6 solution

def allFactors(num):
    nums = []
    for i in range(2, num//2):
        if num / i % 1 == 0:
            pair = sorted((i, num//i))
            pair.reverse()
            if (pair in nums): continue
            nums.append(pair)
    return nums

def main():
    num = int(input())
    nums = allFactors(num)
    for pair in nums:
        print(f"{pair[0]} x {pair[1]}")

if __name__ == "__main__":
    main()