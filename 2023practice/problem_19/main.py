#Problem 19 solution
def main():
    word = input()
    size = int(input())

    grid = [[' ' for x in range(size)] for y in range(size)]

    counter = 0
    start = [0, 0]

    for x in range(size):
        start[0] = x
        grid[start[1]][start[0]] = word[counter]
        counter += 1
        counter %= len(word)
    
    for y in range(1, size):
        start[1] = y
        grid[start[1]][start[0]] = word[counter]
        counter += 1
        counter %= len(word)
    
    for x in range(size - 2, -1, -1):
        start[0] = x
        grid[start[1]][start[0]] = word[counter]
        counter += 1
        counter %= len(word)
    
    for y in range(size - 2, 0, -1):
        start[1] = y
        grid[start[1]][start[0]] = word[counter]
        counter += 1
        counter %= len(word)
    
    for level in grid:
        print(''.join(level))

if __name__ == "__main__":
    main()