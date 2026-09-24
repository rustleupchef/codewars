#Problem 1 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    print("Welcome to HPE CodeWars, Crunchy Cat! Don't worry! It's going to be fun!")

if __name__ == "__main__":
    main()