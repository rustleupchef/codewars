#Problem 5 solution
def main():
    digits = int(input())

    nums = []
    while True:
        line = input()
        if line == "000":
            break
        nums.append(line)
    
    for num in nums:
        parts = num.split(".")
        print(f"{parts[0]}.{parts[1][:digits]}")

if __name__ == "__main__":
    main()