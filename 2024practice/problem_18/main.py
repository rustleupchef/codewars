#Problem 18 solution
def main():
    bounds = input().split()
    width, height = int(bounds[0]), int(bounds[1])

    text = ""
    for _ in range(height + 2):
        text += input() + "\n"

    text = text.split("\n")[:-3]
    text = [line[4:-1] for line in text]
    
    abc = "abcdefghijklmnopqrstuvwxyz".upper()

    indice = 2
    for i in range(width):
        xs = [line[indice] for line in text]
        counter = xs.count("X")
        print(f"{abc[i]}: {counter}")
        indice += 3


if __name__ == "__main__":
    main()