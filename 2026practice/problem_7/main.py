#Problem 7 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    count = int(input())

    lines = []
    for i in range(count):
        line = input()
        lines.append(line)

    for line in lines:
        components = [tuple(num.split(".")) for num in line.split()]

        part1 = components[0]
        part2 = components[1]

        if ".".join(part1) == ".".join(part2):
            print(".".join(part2) + " is identical")
            continue

        isGreater = False

        for i in range(len(part1)):
            num1 = int(part1[i])
            num2 = int(part2[i])

            if num2 < num1:
                break

            if num2 > num1:
                isGreater = True
                break

        if isGreater:
            print(".".join(part2) + " is newer")
        else:
            print(".".join(part2) + " is older")


        


if __name__ == "__main__":
    main()