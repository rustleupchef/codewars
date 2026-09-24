#Problem 4 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    print(int(input()) * 2)

if __name__ == "__main__":
    main()