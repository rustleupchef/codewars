#Problem 4 solution
def main():
    breakChar = input()
    text = input()
    text = text.replace(breakChar, "\n")
    print(text)

if __name__ == "__main__":
    main()