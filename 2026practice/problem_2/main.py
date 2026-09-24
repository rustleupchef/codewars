#Problem 2 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    print(f"Meme fixed? {input()}, Bet!")

if __name__ == "__main__":
    main()