#Problem 3 solution
def main():
    nums = []
    while True:
        number = int(input())
        if number == -1:
            break
        nums.append(number)

    for num in nums:
        if num == 1:
            print("You, 1 minute ago")
        else:
            print(f"You, {num} minutes ago")

if __name__ == "__main__":
    main()