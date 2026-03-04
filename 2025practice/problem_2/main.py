#Problem 2 solution
def main():
    formatText = ""
    collected = ""
    text = input()
    counter = 0
    for character in text:
        if counter % 3 != 2:
            formatText += character
        else:
            collected += character
        counter += 1
    print(formatText)
    print(collected)

if __name__ == "__main__":
    main()