#Problem 14 solution

def grabAllLengths(target: int):
    pairs = []
    for i in range(target):
        square1 = i ** 2
        square2 = target - square1

        if square2 < 0:
            continue
        
        if square2 ** 0.5 % 1 == 0:
            pair = sorted((i, int(square2 ** 0.5)))
            if not pair in pairs: pairs.append(pair)
    return pairs

def main():
    num = int(input())
    pairs = grabAllLengths(num)

    if len(pairs) <= 0:
        print("That diagonal does not lead to integer sides!")
        return

    pairs = sorted(pairs, key= lambda x: x[0] * x[1])
    print(" ".join([str(x) for x in pairs[-1]]))


if __name__ == "__main__":
    main()