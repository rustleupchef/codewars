#Problem 7 solution
def main():
    nums = []
    while True:
        line = input()
        if line == "0":
            break
        nums.append(int(line))
    
    for num in nums:
        text = f"{num}"
        if num % 5 == 0:
            text += " FIZZ"
        if num % 9 == 0:
            text += " FUZZ"
        if num % 5 == 0 and num % 9 == 0:
            text += "!"
        print(text)

if __name__ == "__main__":
    main()