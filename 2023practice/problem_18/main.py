#Problem 18 solution
def main():
    sep = input().lower()

    ingredients = []
    while True:
        try:
            ingredients.append(input())
        except EOFError:
            break
    
    text = ", ".join([ingredients[i] if i != len(ingredients) - 1 else f"{sep} {ingredients[i]}" for i in range(len(ingredients))])
    
    if len(ingredients) <= 2:
        text = text.replace(',', '')

    if len(ingredients) > 1:
        print(text)
    else:
        print(ingredients[0])

if __name__ == "__main__":
    main()