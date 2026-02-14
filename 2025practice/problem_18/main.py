#Problem 18 solution
def main():
    nums = [int(x) for x in input().split(",")]
    pair = nums[:2]

    proportion = pair[-1] / pair[0]
    difference = pair[-1] - pair[0]

    test = [pair[0]]
    for i in range(1, len(nums)):
        test.append(int(nums[i - 1] + difference))
    
    if nums == test:
        print(f"Sequence: {int(difference) if difference < 0 else '+' + str(difference)}")
        print(f"Next: {int(nums[-1] + difference)}")
        return

    test = [pair[0]]
    for i in range(1, len(nums)):
        test.append(int(nums[i - 1] * proportion))
    
    if nums == test:
        pRep = int(proportion) if proportion > 1 else int(1/proportion)
        print(f"Sequence: {'/' + str(pRep) if difference < 1 else '*' + str(pRep)}")
        print(f"Next: {int(nums[-1] * proportion)}")
        return

    print(f"Sequence: UNKNOWN")
    print(f"Next: UNKNOWN")


if __name__ == "__main__":
    main()