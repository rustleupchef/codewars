#Problem 16 solution

def toMiles(parts):
    conversions = {
        "ft" : (5280, "miles"),
        "in" : (12, "ft"),
        "m" : (.3048, "ft"),
        "y" : (1/3, "ft")
    }

    pair = conversions[parts[1]]
    number = parts[0]/pair[0]
    if pair[1] == "miles":
        return (number, parts[1])
    else:
        toMiles((number, parts[1]))


def main():
    parts = input().split()
    seconds = int(input())

    parts[0] = int(parts[0])
    miles = toMiles(parts)
    
    print(f"{miles[0]/(seconds/3600):.2f}")

if __name__ == "__main__":
    main()