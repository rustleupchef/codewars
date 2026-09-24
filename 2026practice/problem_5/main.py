#Problem 5 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    name = input()
    value = int(input())

    dict = {
        "Bop" : False,
        "Pull" : True,
        "Twist" : value == 0
    }

    print(int(dict[name]))

if __name__ == "__main__":
    main()