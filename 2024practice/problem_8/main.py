#Problem 8 solution
def main():
    line = input()

    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    
    nums.sort()

    text = ""
    for char in line:
        if char.isdigit():
            text += str(nums.pop(0))
        else:
            text += char
    print(text)

if __name__ == "__main__":
    main()