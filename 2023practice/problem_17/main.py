#Problem 17 solution
def main():
    line = input()

    pattern = line[0]

    for i in range(1, len(line)):
        index = line[len(pattern):].index(pattern)
        if index == 0:
            break
        pattern = line[:i + 1]
    
    print(f"{pattern[len(line)%len(pattern):]}")
    print(pattern)

if __name__ == "__main__":
    main()