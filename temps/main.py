import os

def main():
    problems: int
    while True:
        try:
            problems = int(input("Number of problems:"))
            break
        except ValueError:
            print("Please enter valid number of problems")
    problems += 1
    length:int = len(str(problems))
    for i in range(problems):
        zeros = "0" * (length - len(str(i)))
        if not os.path.exists(f"{zeros}{i}.py"):
            with open(f"{zeros}{i}.py", 'x') as file:
                file.close();
    
if __name__ == '__main__':
    main()
    os.remove(__file__)