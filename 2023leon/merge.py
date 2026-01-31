import os

def main():
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    problem_dirs = [d for d in os.listdir(parent_dir) if os.path.isdir(os.path.join(parent_dir, d)) and d.startswith("problem_")]

    text = ""
    for i in range(len(problem_dirs)):
        with open(os.path.join(parent_dir, problem_dirs[i], "description.md"), "r") as f:
            text += f"\n# Problem {i + 1}\n\n{f.read()}"
            f.close()

    with open(os.path.join(parent_dir, "merged.md"), "w") as f:
        f.write(text)
        f.close()

if __name__ == "__main__":
    main()
    os.remove(__file__)