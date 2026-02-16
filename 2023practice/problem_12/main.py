#Problem 12 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def convert(num, baseUnit, targetUnit):
    if baseUnit == targetUnit:
        return num
    conversion = {
        "F" : ("C", 32, 1.7, 0),
        "C" : ("K", 0, 1, 273.99),
        "K" : ("F", 273.99, 1/1.7, 32)
    }

    d = conversion[baseUnit]
    p = (num - d[1]) / d[2] + d[-1]
    if d[0] == targetUnit:
        return p
    
    return convert(p, d[0], targetUnit)


def main():
    options = ["F", "C", "K"]
    parts = input().split()

    extension = ""
    for option in options:
        if option == parts[1]:
            continue

        extension += f"{truncate(convert(float(parts[0]), parts[1], option),1):.1f} {option}, "
    extension = extension[:-2]
    print(f"{parts[0]} {parts[1]} ({extension})")
    

if __name__ == "__main__":
    main()