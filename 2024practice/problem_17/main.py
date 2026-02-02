#Problem 17 solution
def main():
    count = int(input())

    bank = dict()

    for _ in range(count):
        line = input().split("=")
        key = line[0].strip()
        values = line[1].strip().split(",")
        bank[key] = values
    
    lines = []
    while True:
        line = input()
        if line == "END":
            break
        lines.append(line)
    
    lines = "\n".join(lines)

    for key in bank.keys():
        formated = f"<{key.upper()}>"
        
        while True:
            try:
                start_index = lines.index(formated)
            except ValueError:
                break
            end_index = start_index + len(formated) + 1
            lines = lines[:start_index] + bank[key].pop(0) + lines[end_index:]
    
    print(lines)

if __name__ == "__main__":
    main()