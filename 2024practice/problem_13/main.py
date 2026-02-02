#Problem 13 solution
def main():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break
    
    width = len(max(lines, key=len))
    height = len(lines)

    generate = ""

    for y in range(height):
        for x in range(width):
            if x == width - 1 or y == height - 1 or x == 0 or y == 0:
                generate += "#"
            else:
                generate += " "
        generate += "\n"
    
    count = generate.count("#")

    if count != "".join(lines).count("#"):
        print(generate)
    else:
        print("Nothing to do")

if __name__ == "__main__":
    main()