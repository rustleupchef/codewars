#Problem 12 solution
def main():
    parts = [int(x) for x in input().split()]
    first = parts[0] & parts[1]
    seconds = first | parts[2]
    print(first, seconds)

if __name__ == "__main__":
    main()