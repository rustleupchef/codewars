#Problem 2 solution
def main():
    formatText = ""
    text = input()
    counter = 0
    for character in text:
        if counter % 3 != 2:
            formatText += character
        counter += 1
    print(formatText)

if __name__ == "__main__":
    main()