#Problem 7 solution
def main():
    nums = [int(c) for c in input()]
    repeats = {}
    for num in nums:
        if num in repeats:
            repeats[num] += 1
        else:
            repeats[num] = 0
    
    print(f"{min(repeats, key=repeats.get)}: {repeats.get(min(repeats, key=repeats.get))}")

if __name__ == "__main__":
    main()