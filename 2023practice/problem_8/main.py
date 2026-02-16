#Problem 8 solution
def main():
    base = int(input())
    value = int(input())

    exponent = 0
    while True:
        if base ** exponent == value:
            print(f"{base}^{exponent} = {value}")
            break
        exponent += 1

if __name__ == "__main__":
    main()