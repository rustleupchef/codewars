#Problem 20 solution
def main():
    lines = []

    while True:
        line = input()
        if line == "END":
            break
        lines.append(line.split(","))
    

    text = ""

    for line in lines:
        text += line[0] + "\n"
        text += line[1][1:] + "\n"
        text += f"{line[2][1:]},{line[3]}{line[-1]}\n\n"
    
    print(text[:-2])

if __name__ == "__main__":
    main()