#Problem 7 solution
def main():
    line = input().strip()

    current = None
    count = 0

    text = ""

    for char in line:
        if char == current:
            count += 1
            if count == 4:
                text += char
                count = 0
        else:
            current = char
            count = 1

    print(text)
if __name__ == "__main__":
    main()