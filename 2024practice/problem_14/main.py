#Problem 14 solution
def main():
    nums = input().split()
    checksum = float(input().split('=')[1])

    valid_nums = []
    for num in nums:
        try:
            if float(num) <= checksum:
                valid_nums.append(float(num))
        except ValueError:
            continue
    
    print(" ".join([str(x) for x in valid_nums]))

    lengthCount = max([len(str(x).split('.')[1]) if '.' in str(x) else 0 for x in valid_nums])
    
    if checksum == round(sum(valid_nums), lengthCount):
        print("CHECKED")
    else:
        print("BADCHECK:" + str(round(sum(valid_nums), lengthCount)))

if __name__ == "__main__":
    main()