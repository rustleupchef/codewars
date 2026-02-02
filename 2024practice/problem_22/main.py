#Problem 22 solution

def calc(x, m, b):
    return int(m * x + b)

def printGrid(grid):
    for row in grid:
        print(''.join(row))

def main():
    
    nums = [int(x) for x in input().split()]
    m = nums[0]
    b = nums[1]
    size = nums[2]

    print(f"y = {m}x + {b}")

    width = size * 2 + 2
    height = size + 1

    grid = [[' ' for _ in range(width)] for _ in range(height)]

    for y in range(height):
        if y == 0:
            grid[-1][0] = "0"
            grid[-1][1] = "#"
            continue

        point = str(y)
        if len(point) < 2:
            point = "0" + point
        
        grid[-(y+1)][0] = point[0]
        grid[-(y+1)][1] = point[1]

        grid[-1][y * 2] = point[0]
        grid[-1][1 + y * 2] = point[1]

        y1 = calc(y, m, b)
        if (y1 > size or y1 < 0):
            continue
        if (m == 0):
            grid[-1 - y1][1 + y * 2] = "-"
            continue
        grid[-1 - y1][1 + y * 2] = "#"
    
    printGrid(grid)

if __name__ == "__main__":
    main()