#Problem 13 solution
def main():
    lines = []
    while True:
        line = input()
        if line == "0":
            break
        lines.append(line)
    
    for line in lines:
        line = line[::-1]
        text = ""
        counter = 0
        for character in line:
            character: str
            if not character.isdigit():
                text += character
                continue
            
            if counter >= 4:
                text += 'x'
                continue

            text += character
            counter += 1
        print(text[::-1])

if __name__ == "__main__":
    main()