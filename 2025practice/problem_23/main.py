#Problem 23 solution
def main():
    top, middle, bottom = [int(input()) for i in range(3)]

    lines = []
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    width = max([len(line) for line in lines])
    used = set()

    topLines = []
    for line in lines:
        line: str
        size = line.count(" ")
        if top >= size and not size in used:
            topLines.append(size)
            used.add(size)

    middleLines = []
    for line in lines:
        line: str
        size = line.count(" ")
        if middle >= size and not size in used:
            middleLines.append(size)
            used.add(size)

    bottomLines = []
    for line in lines:
        line: str
        size = line.count(" ")
        if bottom >= size and not size in used:
            bottomLines.append(size)
            used.add(size)

    topLines.sort()
    del topLines[0]
    middleLines.sort()
    bottomLines.sort()

    topLines.extend(topLines[:-1][::-1])
    middleLines.extend(middleLines[:-1][::-1])
    bottomLines.extend(bottomLines[:-1][::-1])

    groups = [topLines, middleLines, bottomLines]

    print(f"T{'#' * (width - 1)}")
    for group in groups:
        for line in group:
            print([d for d in lines if d.count(' ') == line][0])
    print(f"B{'#' * (width - 1)}")


if __name__ == "__main__":
    main()
