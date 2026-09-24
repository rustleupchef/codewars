#Problem 8 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    base = input()

    lines = []
    while True:
        line = input()

        if line == ".": break

        lines.append(line)

    wrongs = [line for line in lines if line != base]
    if len(wrongs) > 0:
        print("\n".join(wrongs))
    print(f"Number of incorrect lines: {len(wrongs)}")

if __name__ == "__main__":
    main()