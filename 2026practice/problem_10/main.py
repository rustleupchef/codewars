#Problem 10 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    LR = "One ring to rule them all, one ring to find them,\nOne ring to bring them all and in the darkness bind them".split()
    GA = "Four score and seven years ago our fathers brought forth,\nupon this continent, a new station".split()
    RT = "The quick brown fox, jumps over the lazy dog. Wars in 2026 have many En-Code-ings.\n29! = 29*28*27! ABCde FGHIJ KLMno pqrst UVWXY 123456789?".split()

    letters = [letter.split("-") for letter in input().split()]

    for letter in letters:
        text, word, character = letter
        word = int(word) - 1
        character = int(character) - 1
        cText = eval(text)

        if character >= 0 and word >= 0:
            print(cText[word][character], end="")
            continue

        if word == -1:
            print(" ", end="")
            continue

        if character == -1:
            print(cText[word], "", end="")
            continue
    print()

if __name__ == "__main__":
    main()