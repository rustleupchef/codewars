#Problem 15 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def generate_sequence(base: list[int], points: list[int]):
    nums = base
    base_string = "".join(str(num) for num in nums)

    for i in range(max(points)):
        num = nums[-1] + nums[-2]
        nums.append(num)

        base_string += str(num)

    return [base_string[point - 1] for point in points]

def main():
    nums = list(map(int, input().split()))
    base = nums[:2]
    values = nums[2:]

    sequence = generate_sequence(base, values)
    print(" ".join([str(num) for num in sequence]))
    

if __name__ == "__main__":
    main()