#Problem 16 solution
def main():
    nums = []

    while True:
        num = int(input())
        if num == 0:
            break
        nums.append(num)
    
    counter = dict()

    for n in nums:
        if n in counter:
            counter[n] += 1
        else:
            counter[n] = 1
    
    print(f"{max(counter, key=counter.get)} [{counter[max(counter, key=counter.get)]} count]")
    counter.pop(max(counter, key=counter.get))
    print(f"{max(counter, key=counter.get)} [{counter[max(counter, key=counter.get)]} count]")

if __name__ == "__main__":
    main()