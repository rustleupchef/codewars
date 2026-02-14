#Problem 11 solution
def main():
    temp = ""

    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append([x.strip() for x in line.split("=")])
    
    for line in lines:
        temp += f"{' ' * 4}\"{line[0]}\":\"{line[1]}\",\n"
    temp = "{\n" + temp[:-2] + "\n}"
    print(temp)

if __name__ == "__main__":
    main()