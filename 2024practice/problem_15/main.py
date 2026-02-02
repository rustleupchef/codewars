#Problem 15 solution
def main():
    top = ""
    bottom = ""

    chemical = input().split()[0]

    for char in chemical:
        if char.isdigit():
            top += " "
            bottom += char
            continue
        else:
            top += char
            bottom += " "
    print(top)
    print(bottom)

if __name__ == "__main__":
    main()