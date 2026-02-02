#Problem 23 solution

def bounds(points) -> tuple:
    widths = []
    heights = []

    for p1 in points:
        for p2 in points:
            if p1 == p2:
                continue
            widths.append(abs(p1[0] - p2[0]))
            heights.append(abs(p1[1] - p2[1]))
        
    return (max(widths), max(heights))

def quadrilateralDefine(points) -> str:
    pass
    

def main():
    points = []

    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "#":
                points.append((x, y))
    
    match len(points):
        case 3:
            print(f"Triangle with width {bounds(points)[0]} and height {bounds(points)[1]}")
        case 4:
            shape = quadrilateralDefine(points)
            print(f"{shape}")
        case 5:
            print("Pentagon")
        case 6:
            print("Hexagon")
        case _:
            print("Polygon with more than 6 sides")

if __name__ == "__main__":
    main()