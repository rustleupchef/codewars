grid = input()
grid.split('\n')

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'A':
            print(f"Get out of there! Danger at ({x}, {y})")
            break
else:
    print("You are lucky Get back to the office NOW!")