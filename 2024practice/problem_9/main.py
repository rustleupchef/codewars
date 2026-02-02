#Problem 9 solution
def main():
    lines = []

    while True:
        line = input()
        if line == "STOP":
            break
        lines.append(line)
    
    abc = "abcdefghijklmnopqrstuvwxyz"
    for line in lines:
        for c in abc:
            line = line.replace(c * 2, c.lower())
            line = line.replace(c.upper() * 2, c.upper())
        print(line)

if __name__ == "__main__":
    main()