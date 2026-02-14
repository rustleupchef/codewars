#Problem 19 solution
def main():
    vowels = "aeiou"
    text = ""
    while True:
        line = input()
        if line == "END":
            break
        text += line + " "
    text = text.lower()

    combos = []

    counter = 0
    for i in range(len(text)):
        character = text[i]
        if character in vowels:
            counter += 1
            if counter == 2:
                if i == len(text) - 1:
                    combos.append(character + text[i - 1])
                    continue
                if not text[i + 1] in vowels: combos.append(character + text[i - 1])
            continue
        counter = 0
    
    combosCount = dict()
    for combo in combos:
        combosCount[combo] = combosCount[combo] + 1 if combo in combosCount else 1
    
    for combo in combosCount.keys():
        print(f"{combo[::-1]}: {combosCount.get(combo)}")

if __name__ == "__main__":
    main()