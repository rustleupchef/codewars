import sys
import os

def main(arguments:list[str] = []):
    count = 0
    count = int(arguments[0]) if len(arguments) > 0 else count

    print(f"Designing file for {count} problem(s)")

    with open("temps/templates/main.py", "r") as f:
        template = f.read()
        f.close()

    for i in range(count + 1):
        print("-" * 20)
        print(f"Working on problem {i}")

        os.path.exists("working") or os.makedirs("working")
        os.makedirs(f"working/problem_{i}/", exist_ok=True)
        with open(f"working/problem_{i}/input.txt", "w") as f:
            f.close()

        with open(f"working/problem_{i}/main.py", "w") as f:
            f.write(f"#Problem {i} solution\n{template}")
            f.close()

if __name__ == "__main__":
    main(sys.argv[1:])