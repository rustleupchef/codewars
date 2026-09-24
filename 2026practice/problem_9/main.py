#Problem 9 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def shiftCharacter(shift: int, character: str):
    isUpper = character.upper() == character

    abc = "abcdefghijklmnopqrstuvwxyz"
    abc = abc.upper() if isUpper else abc.lower()

    return abc[(abc.index(character) + shift) % len(abc)]

def main():
    shift = int(input())
    text = input()

    characters = []

    for character in text:
        if character.isalpha():
            characters.append(shiftCharacter(shift, character))
        else:
            characters.append(character)
        
    print("".join(characters))

if __name__ == "__main__":
    main()