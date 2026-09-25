#Problem 20 solution
import math
import itertools

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    first, second, third = input().split("-")
    letters = dict([[segment for segment in var.split("=")]for var in input().split()])

    nums = [None for i in range(10)]

    combined = first + second + third
    for i in range(len(combined)):
        if combined[i] in letters:
            nums[i] = letters[combined[i]]
    left = [str(i) for i in range(10) if not (str(i) in nums)]

    versions = list(itertools.permutations(left))
    for version in versions:
        position = 0
        template_nums = nums[:]
        for i in range(len(template_nums)):
            if template_nums[i] == None:
                template_nums[i] = version[position]
                position += 1
        num1 = "".join(template_nums[:3])
        num2 = "".join(template_nums[3:6])
        num3 = "".join(template_nums[6:])

        if num1[0] == "0" or num2 == "0":
            continue

        if int(num1) + int(num2) == int(num3):
            print("-".join((first, second, third)), "=", "-".join((num1, num2, num3)))
            break

    

if __name__ == "__main__":
    main()