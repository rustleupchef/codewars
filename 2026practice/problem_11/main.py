#Problem 11 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    nums = [1 - float(num) for num in input().split()]
    line = input()

    v1 = nums[0]
    v2 = nums[1]
    v3 = nums[2]

    final: float = 1

    for character in line:
        final *= v1 if character == "1" else v2

    print(f"{truncate(final, 3):.3f}")
    print("reject" if final < v3 else "accept")
    

if __name__ == "__main__":
    main()