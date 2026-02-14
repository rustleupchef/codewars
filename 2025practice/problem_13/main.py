#Problem 13 solution
def allFactors(num):
    nums = []
    for i in range(2, num):
        if num % i == 0:
            nums.append(i)
    nums.sort()
    nums.reverse()
    return nums

def main():
    pairs = []
    while True:
        line = input()
        if line == "0 0":
            break
        pairs.append([int(x) for x in line.split()])

    for pair in pairs:
        remainder = pair[0] % pair[1]
        whole = int((pair[0] - remainder)/pair[1])

        GCD = 1
        denominatorNums = allFactors(pair[1])

        for num in denominatorNums:
            if remainder % num == 0:
                GCD = num
                break
        
        proportion = f"{remainder//GCD}/{pair[1]//GCD}"
        output = [str(whole if whole != 0 else None), str(proportion if remainder != 0 else None)]
        output = [x for x in output if x != "None"] 
        print(" ".join(output))



if __name__ == "__main__":
    main()