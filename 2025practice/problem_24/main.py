#Problem 24 solution
def int_to_base(n, base):
    if n == 0:
        return "0"
    digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    result = ""
    while n > 0:
        n, remainder = divmod(n, base)
        result = digits[remainder] + result
    return result

def main():
    x, y, z = [input() for _ in range(3)]
    text = input().split()

    print(".".join([int_to_base(ord(c), 3) for c in x]))
    print(".".join([int_to_base(ord(c), 3) for c in y]))
    print(".".join([int_to_base(ord(c), 3) for c in z]))

    text = ["".join([chr(int(c, 3)) for c in word.split(".")]) for word in text]
    print(" ".join(text))

if __name__ == "__main__":
    main()