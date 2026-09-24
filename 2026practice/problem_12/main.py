#Problem 12 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    with open("files/probBQ/EyeDiagram.txt", "r") as f:
        text = f.read()

    base_grid = [[cell for cell in row.split()] for row in text.split("\n")]
    grid = [[cell for cell in input().split()] for i in range(6)]
    isSuccess = True
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if base_grid[i][j] == "O" and grid[i][j] == "-":
                grid[i][j] = "!"
                isSuccess = False

    print("PASS" if isSuccess else "FAIL")

    if not isSuccess:
        for row in grid:
            print(" ".join(row))
    

if __name__ == "__main__":
    main()