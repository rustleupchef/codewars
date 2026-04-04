import sys
import os

def main(arguments = []):
    if len(arguments) <= 0:
        print("Usage: python extract.py <output_path> [working_path]")
        return
    output_path = arguments[0]
    working_path = arguments[1] if len(arguments) > 1 else "working"

    folders = os.listdir(working_path)
    for folder in folders:
        if not folder.startswith("problem_"):
            continue

        problem_num = folder.split("_")[1]
        inputs_path = os.path.join(working_path, folder, "inputs")
        outputs_path = os.path.join(working_path, folder, "outputs")

        for input_file in os.listdir(inputs_path):
            if not input_file.startswith("input"):
                continue
            input_num = input_file.split("input")[1].split(".")[0]
            with open(os.path.join(inputs_path, input_file), 'r') as f:
                input_text = f.read()
                f.close()

            with open(os.path.join(output_path, f"prob{problem_num.zfill(2)}-{input_num}-in.txt"), "w") as f:
                f.write(input_text)
                f.close()
        
        for output_file in os.listdir(outputs_path):
            if not output_file.startswith("output"):
                continue
            output_num = output_file.split("output")[1].split(".")[0]
            with open(os.path.join(outputs_path, output_file), 'r') as f:
                output_text = f.read()
                f.close()

            with open(os.path.join(output_path, f"prob{problem_num.zfill(2)}-{output_num}-out.txt"), "w") as f:
                f.write(output_text)
                f.close()

if __name__ == "__main__":
    main(sys.argv[1:])