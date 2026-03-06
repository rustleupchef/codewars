#Problem 26 solution
def grabFactors(num: int, needs=tuple()):
    factors = []
    for i in range(1, num + 1):
        if i == 1 or i == num:
            continue
        if num % i == 0:
            factors.append(sorted(needs + (i, num // i)))
            seed1 = grabFactors(i, needs + (num // i, ))
            if seed1:
                factors.extend(sorted(seed1))
    return tuple(factors)

def main():
    nums = []
    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)

    for num in nums:
        factors = grabFactors(num)
        filters = []

        for factor in factors:
            if factor[::-1] not in filters:
                filters.append(factor[::-1])
        filters = sorted(filters, key=lambda x: x[0])[::-1]
        if filters == []:
            continue
        filters = [[str(x) for x in combo] for combo in filters]
        combinations = [f'({"*".join(combo)})' for combo in filters]
        print(f"{num}={','.join(combinations)}")

if __name__ == "__main__":
    main()
