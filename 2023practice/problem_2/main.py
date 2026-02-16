#Problem 2 solution
def main():
    nums = []

    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    
    for num in nums:
        if num % 4 != 0: continue
        print(f"{num}/4 = {num//4}")

if __name__ == "__main__":
    main()