import sys
import os

def main(arguments:list[str] = []):
    count = 0
    count = int(arguments[0]) if len(arguments) > 0 else count

    print(f"Designing file for {count} problem(s)")
    for i in range(count):
        print("-" * 20)
        print(f"Working on problem {i + 1}")

        os.path.exists("working") or os.makedirs("working")
        os.makedirs(f"working/problem_{i + 1}/", exist_ok=True)
        with open(f"working/problem_{i + 1}/input.txt", "w") as f:
            f.close()

        with open(f"working/problem_{i + 1}/main.py", "w") as f:
            f.write(f"#Problem {i +1} solution\ndef main():\n    pass\n\nif __name__ == \"__main__\":\n    main()\n")
            f.close()

if __name__ == "__main__":
    main(sys.argv[1:])