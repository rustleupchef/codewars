#Problem 6 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    text = input()
    odds = "".join([text[i] for i in range(len(text)) if i % 2 == 0])
    evens = "".join([text[i] for i in range(len(text)) if i % 2 != 0])

    print(f"{odds}{evens}")

if __name__ == "__main__":
    main()