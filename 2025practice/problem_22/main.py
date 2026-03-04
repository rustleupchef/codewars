#Problem 22 solution
import itertools

def get_combinations():
    return list(itertools.permutations(range(1, 8)))

def main():
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)

    combinations = get_combinations()
    combinations = [
        int("".join([str(x) for x in combination]))
        for combination in combinations
    ]
    combinations = [
        combination for combination in combinations if combination % 11 == 0
    ]
    combinations.sort()

    for num in nums:
        print(combinations[num - 1])


if __name__ == "__main__":
    main()
