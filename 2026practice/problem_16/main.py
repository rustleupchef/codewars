#Problem 16 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def op(num1, num2, op_code):
    val1 = bool(int(num1))
    val2 = bool(int(num2))

    if op_code == "01":
        return int(val1 or val2)
    
    if op_code == "10":
        return int(val1 and val2)

    if op_code == "11":
        return int((val1 or val2) and not (val1 and val2))

def main():
    val1, val2, opcode = input().split()

    if opcode == "00":
        val3 = int(val1, 2) + int(val2, 2)
        val3 = bin(val3)[2:]
        val3 = f"{'0' * (5 - len(val3))}{val3}"
        carry = val3[0]
        val3 = val3[1:]
        print(val3, carry)
        return

    nums = []
    for i in range(4):
        nums.append(str(op(val1[i], val2[i], opcode)))
    print("".join(nums), 0)

if __name__ == "__main__":
    main()