#Problem 10 solution
def main():
    lines = []

    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    for line in lines:
        line = line.replace("+", ",")
        line = line.replace("=", ",")

        nums = [int(num) for num in line.split(",")]
        result = sum(nums[:-1])

        if result == nums[-1]:
            print("CORRECT")
        else:
            print(f"WRONG: {nums[0]}+{nums[1]}={result}")

if __name__ == "__main__":
    main()