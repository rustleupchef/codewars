#Problem 6 solution
def main():
    lines = []
    while True:
        line = input()
        if line == "0 0 S":
            break
        lines.append(line.split())
    
    for parts in lines:
        w = int(parts[0])
        h = int(parts[1])
        t = parts[2]

        if t == "S":
            print(f"Square {2 * (h + w) + 80}")
        else:
            print(f"Diagonal {2 * (h + w) + 320}")

if __name__ == "__main__":
    main()