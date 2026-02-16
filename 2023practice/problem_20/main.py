#Problem 20 solution
def main():
    base = int(input())

    nums = [2 ** i for i in range(9, -1, -1)]
    valid = []

    remainer = base
    for num in nums:
        if remainer >= num:
            print(f"{num}=1")
            remainer -= num
            valid.append(num)
        else:
            print(f"{num}=0")
    
    finale = ''.join(['1' if x in valid else '0' for x in nums])
    finale = finale[finale.index('1'):]

    if len(valid) < 2:
        print(f"{base} = {finale}")
        return
    
    sum = valid[0] + valid[1]
    print(f"{valid[0]}+{valid[1]} = {sum}")

    for i in range(2, len(valid)):
        print(f"{sum}+{valid[i]} = {sum + valid[i]}")
        sum += valid[i]

    print(f"{base} = {finale}")



if __name__ == "__main__":
    main()