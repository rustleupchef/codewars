#Problem 15 solution
def main():
    num = input()

    counts = dict()
    for character in num:
        counts[character] = counts[character] + 1 if character in counts else 1
    
    mxNum = float(max(counts, key=counts.get))
    
    correct = sum([int(c) for c in num])/len(num) == mxNum
    
    print(f"{num} ORIGINAL")

    if correct:
        print(f"{''.join([str(int(x) - int(mxNum)) if int(x) > mxNum else '0' for x in num])} SUBTRACTED")
        print(f"{''.join([str(abs(int(x) - int(mxNum))) if int(x) < mxNum else '0' for x in num])} ADDED")
        print(f"{str(int(mxNum)) * len(num)} FINAL")
    else:
        print(f"{''.join([str(int(x) - int(mxNum)) if int(x) > mxNum else '0' for x in num])} AVAILABLE")
        print(f"{''.join([str(abs(int(x) - int(mxNum))) if int(x) < mxNum else '0' for x in num])} NEEDED")
        print(f"{str(int(mxNum)) * len(num)} IMPOSSIBLE")

if __name__ == "__main__":
    main()