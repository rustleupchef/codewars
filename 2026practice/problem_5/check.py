#Problem 5 checker
import subprocess
import os
import sys
import difflib

def main():
    highestIn = max([int(f.split(".")[0][-1]) for f in os.listdir("inputs")])
    highestOut = max([int(f.split(".")[0][-1]) for f in os.listdir("inputs")])

    highest = min(highestIn, highestOut)
    for i in range(1, highest + 1):
        with open(f"inputs/input{i}.txt", "r") as f:
            result = subprocess.run([sys.executable, "main.py"], stdin=f, capture_output=True, text=True)
            output = result.stderr if result.stderr else result.stdout
            f.close()
        
        with open(f"outputs/output{i}.txt", "r") as f:
            outputCheck = f.read()
            f.close()
        
        diff = difflib.Differ().compare(output.split("\n"), outputCheck.split("\n"))
        print("\n".join(diff))
        print(f'Test {i}: {"✅" if outputCheck == output else "❎"}')
        

    

if __name__ == "__main__":
    main()