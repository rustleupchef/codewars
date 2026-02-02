#Problem 11 solution
def main():
    lines = []

    while True:
        line = input()
        if line == "0 0":
            break
        lines.append([int(x) for x in line.split()])
    
    seconds = lines[0][0]
    nanoseconds = lines[0][1]

    total_nanoseconds = seconds * 1_000_000_000 + nanoseconds

    for i in range(1, len(lines)):
        sec = lines[i][0]
        nano = lines[i][1]

        diff = total_nanoseconds - (sec * 1_000_000_000 + nano)
        print(abs(int(diff / 1_000_000)))
        total_nanoseconds = sec * 1_000_000_000 + nano

if __name__ == "__main__":
    main()