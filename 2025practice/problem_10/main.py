#Problem 10 solution
def main():
    lines = []
    while True:
        line = input()
        if line == "000":
            break
        lines.append(line)
    
    for line in lines:
        print("".join([character.upper() if character.lower() == character else character.lower() for character in line]))

if __name__ == "__main__":
    main()