#Problem 5 solution
def main():
    nums = input().split()
    characters = [chr(int(num)) for num in nums]
    print("".join(characters))

if __name__ == "__main__":
    main()