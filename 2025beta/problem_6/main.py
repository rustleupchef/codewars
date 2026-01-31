#Problem 6 solution
def main():
    # grab all the nums and conver to base 10
    quaternaries = []
    while True:
        num = input()
        if num == "000":
            break
        quaternaries.append(int(num, 4))

    # print all out
    for num in quaternaries:
        print(num)

if __name__ == "__main__":
    main()