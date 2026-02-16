#Problem 9 solution
import math

def truncate(num, decimals):
    return math.trunc(num * (10 ** decimals))/(10 ** decimals)

def main():
    count = int(input())
    hours = int(input())/60

    cars = []

    for i in range(count):
        line = input().split()
        cars.append(line)
    
    for car in cars:
        mph = int(car[0])

        distance = mph * hours

        line = ""

        sRemainder = distance % 5
        fChunks = (distance - sRemainder)/5

        qRemainder = distance % 1
        sChunks = (sRemainder - qRemainder)

        dRemainder = distance % .25
        qChunks = (qRemainder - dRemainder)/.25

        line = '-' * int(fChunks) + '~' * int(sChunks) + "{}" * int(qChunks)
        print(f"({truncate(distance,2):.2f}){line}{car[1]}")


if __name__ == "__main__":
    main()