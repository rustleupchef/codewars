import sys
import os

def main(arguments:list[str] = []):
    count = 0
    working_dir = ""

    count = int(arguments[0]) if len(arguments) > 0 else count
    working_dir = arguments[1] if len(arguments) > 1 else working_dir

    os.makedirs(working_dir, exist_ok=True)

    print(f"Designing file for {count} problem(s)")

    with open("temps/templates/main.py", "r") as f:
        template = f.read()
        f.close()

    with open("temps/templates/description.md", "r") as f:
        description = f.read()
        f.close()
    
    with open ("temps/templates/merge.py", "r") as f:
        merge_script = f.read()
        f.close()

    for i in range(count + 1):
        print("-" * 20)
        print(f"Working on problem {i}")

        os.path.exists(working_dir) or os.makedirs(working_dir)
        os.makedirs(f"{working_dir}/problem_{i}/", exist_ok=True)
        with open(f"{working_dir}/problem_{i}/input.txt", "w") as f:
            f.close()

        with open(f"{working_dir}/problem_{i}/main.py", "w") as f:
            f.write(f"#Problem {i} solution\n{template}")
            f.close()

        with open(f"{working_dir}/problem_{i}/description.md", "w") as f:
            f.write(description)
            f.close()

    with open(f"{working_dir}/merge.py", "w") as f:
        f.write(merge_script)
        f.close()

if __name__ == "__main__":
    main(sys.argv[1:])