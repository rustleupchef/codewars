#Problem 12 solution
def main():
    lines = []

    while True:
        line = input()
        if line == "END END END":
            break
        lines.append(line.split())
    
    pairs = set()
    for line in lines:
        for item in line:
            if item in pairs:
                pairs.remove(item)
            else:
                pairs.add(item)
    
    for item in list(pairs):
        print(item)

if __name__ == "__main__":
    main()