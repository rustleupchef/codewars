#Problem 5 solution
def int_to_base6(n):
    if n == 0:
        return "0"
    digits = []
    base_digits = "012345"
    while n:
        remainder = n % 6
        digits.append(base_digits[remainder])
        n //= 6
    return "".join(digits[::-1])


def main():
    line = input()
    text = ""
    for character in line:
        f = int_to_base6(ord(character))
        f = '0' * (3 - len(f)) + f
        text += f
    print(text)


if __name__ == "__main__":
    main()
