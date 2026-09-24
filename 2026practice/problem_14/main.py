#Problem 14 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def valid(character: str):
    un_valid = [" ", ",", ".", "?", "!"]
    return not character in un_valid

def main():
    lines: list[str] = []

    while True:
        line = input()

        if line == "END":
            break

        lines.append(line)

    for line in lines:
        subs = []
        current_str = ""
        for character in line:
            if not valid(character):
                subs.append(current_str[::-1])
                current_str = ""
                continue
            current_str += character
        subs.append(current_str[::-1])
        long_str = "".join(subs)

        counter = 0
        new_line = ""
        for character in line:
            if valid(character):
                new_line += long_str[counter]
                counter += 1
            else:
                new_line += character
        print(new_line)
                
                

if __name__ == "__main__":
    main()