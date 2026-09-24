#Problem 17 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    num_grid: list[str] = []
    for i in range(13):
        num_grid.append(input())

    num_grid = num_grid[1:-1]
    num_grid = [row.replace("|", "") for row in num_grid]
    num_grid = [row for row in num_grid if not row.startswith("=")]

    num_grid = [[int(cell) for cell in row.split()] for row in num_grid]
    
    incorrect_rows = []
    incorrect_columns = []
    incorrect_sub_grids = []

    for row in range(len(num_grid)):
        uniques = set()
        for col in range(len(num_grid[row])):
            if num_grid[row][col] in uniques:
                incorrect_rows.append(row + 1)
                break
            uniques.add(num_grid[row][col])
    incorrect_rows = [str(row) for row in incorrect_rows]

    for col in range(len(num_grid[0])):
        uniques = set()
        for row in range(len(num_grid)):
            if num_grid[row][col] in uniques:
                incorrect_columns.append(col + 1)
                break
            uniques.add(num_grid[row][col])
    incorrect_columns = [str(col) for col in incorrect_columns]

    sub_grids = []
    for row in range(3):
        for col in range(3):
            sub_grid = [
                num_grid[(row * 3)][(col * 3):(col * 3) + 3],
                num_grid[(row * 3) + 1][(col * 3):(col * 3) + 3],
                num_grid[(row * 3) + 2][(col * 3):(col * 3) + 3]
            ]
            sub_grids.append(sub_grid)

    for i in range(len(sub_grids)):
        flattened_grid = sub_grids[i][0] + sub_grids[i][1] + sub_grids[i][2]
        uniques = set()
        for num in flattened_grid:
            if num in uniques:
                incorrect_sub_grids.append(i + 1)
                break
            uniques.add(num)
    incorrect_sub_grids = [str(sub_grid) for sub_grid in incorrect_sub_grids]

    incorrect = sum([len(inccorects) for inccorects in [incorrect_sub_grids, incorrect_columns, incorrect_rows]]) > 0
    if incorrect:
        print("INCORRECT")
        if not len(incorrect_rows) > 0:
            incorrect_rows.append("0")
        if not len(incorrect_columns) > 0:
            incorrect_columns.append("0")
        if not len(incorrect_sub_grids) > 0:
            incorrect_sub_grids.append("0")

        print(f"Rows: {' '.join(incorrect_rows)}")
        print(f"Columns: {' '.join(incorrect_columns)}")
        print(f"Subgrids: {' '.join(incorrect_sub_grids)}")
    else:
        print("CORRECT")
        
    

if __name__ == "__main__":
    main()