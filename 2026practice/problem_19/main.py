#Problem 19 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    characters = ["*", "/", "-", "+"]

    line: str = input()
    terms: list[str] = []

    current = ""
    for character in line:
        if character.isdigit():
            current += character
        if character in characters:
            terms.extend([current, character])
            current = ""
    terms.append(current)

    while len(terms) > 1:
        end = False
        for i in range(len(terms)):
            if terms[i] in ["*", "/"]:
                product = str(int(eval(f"{terms[i-1]}{terms[i]}{terms[i+1]}")))
                terms = terms[:max(i - 1, 0)] + [product] + terms[min(i + 2, len(terms)):]
                end = True
                break
        if end:
            print("".join(terms)) 
            continue
        
        for i in range(len(terms)):
            if terms[i] in ["+", "-"]:
                product = str(eval(f"{terms[i-1]}{terms[i]}{terms[i+1]}"))
                terms = terms[:max(i - 1, 0)] + [product] + terms[min(i + 2, len(terms)):]
                break
        print("".join(terms))



if __name__ == "__main__":
    main()