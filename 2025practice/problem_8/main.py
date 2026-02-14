#Problem 8 solution
def main():
    word = input()
    character = input().upper()
    count = word.lower().count(character.lower())

    if count == 1:
        print(f"There is 1 {character.upper()} in {word}")
    else:
        print(f"There are {count} {character.upper()}'s in {word}")

if __name__ == "__main__":
    main()