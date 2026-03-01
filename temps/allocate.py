import sys
import os

def main(arguments = []):
    path = arguments[0] if len(arguments) > 0 else ""
    with open("temps/templates/main.py", "r") as f:
        template = f.read()
        f.close()
    with open("temps/templates/check.py", "r") as f:
        check = f.read()
        f.close()

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    indexedFiles = {}
    for file in files:
        indexedFiles[file] = file.removeprefix("prob").split("-")[0]
    files = sorted(files, key=indexedFiles.get)
    
    problem_paths = dict()
    count = 0
    while True:
        problem_paths[count] = [f.removeprefix(f"prob{'0' * (2 - len(str(count)))}{count}-") for f in files if f.startswith(f"prob{'0' * (2 - len(str(count)))}{count}-")]
        if len(problem_paths[count]) <= 0:
            del problem_paths[count]
            break
        count += 1
    
    for i in problem_paths:
        print("-" * 20)
        print(f"Working on problem {i}")

        os.path.exists("working") or os.makedirs("working")
        os.makedirs(f"working/problem_{i}/inputs/", exist_ok=True)
        os.makedirs(f"working/problem_{i}/outputs/", exist_ok=True)

        if not os.path.exists(f"working/problem_{i}/main.py"):
            with open(f"working/problem_{i}/main.py", "w") as f:
                f.write(f"#Problem {i} solution\n{template}")
                f.close()
        
        with open(f"working/problem_{i}/check.py", "w") as f:
            f.write(f"#Problem {i} checker\n{check}")
            f.close()
        
        outs = [f for f in problem_paths[i] if "out" in f]
        ins = [f for f in problem_paths[i] if "in" in f]

        for out in outs:
            outPath = os.path.join(path, f"prob{'0' * (2 - len(str(i)))}{i}-{out}")
            with open(outPath, 'r') as f:
                outText = f.read()
                f.close()

            with open(f"working/problem_{i}/outputs/output{out.split('-')[0]}.txt", "w") as f:
                f.write(outText)
                f.close
        
        for en in ins:
            inPath = os.path.join(path, f"prob{'0' * (2 - len(str(i)))}{i}-{en}")
            with open(inPath, 'r') as f:
                inText = f.read()
                f.close()

            with open(f"working/problem_{i}/inputs/input{en.split('-')[0]}.txt", "w") as f:
                f.write(inText)
                f.close
            

if __name__ == "__main__":
    main(sys.argv[1:])