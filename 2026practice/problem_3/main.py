#Problem 3 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    print(input() * 3)

if __name__ == "__main__":
    main()