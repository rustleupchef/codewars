#Problem 21 solution

def isSorted(word: str) -> bool:
    return word == ''.join(sorted(word))

def vowelSort(word: str) -> bool:
    vowels = "aeiou"

    vowel_chars = [char for char in word if char in vowels]
    return vowel_chars == sorted(vowel_chars)

def consonantSort(word: str) -> bool:
    vowels = "aeiou"
    consonant_chars = [char for char in word if char not in vowels]
    return consonant_chars == sorted(consonant_chars)

def main():
    words = []

    while True:
        word = input()
        if word == "z":
            break
        words.append(word)
    
    for word in words:
        if isSorted(word):
            print(f"{word} SORTED")
        elif consonantSort(word):
            print(f"{word} CONS-SORTED")
        elif vowelSort(word):
            print(f"{word} VOW-SORTED")
        else:
            print(f"{word} UNSORTED")
    


if __name__ == "__main__":
    main()