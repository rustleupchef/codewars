#Problem 4 solution
def main():
    components = input().split()
    name = components[0]

    times = int(components[1])

    shirts = 0
    hats = 0
    stickers = 0

    for i in range(times):
        points = [int(x) for x in input().split()]
        shirts += points[0]
        hats += points[1]
        stickers += points[2]
    
    total = sum([shirts * 13, hats * 9, stickers * 2])

    shirtsText = f"{shirts} shirts" if shirts != 1 else "1 shirt"
    hatsText = f"{hats} hats" if hats != 1 else "1 hat"
    stickersText = f"{stickers} stickers" if stickers != 1 else "1 sticker"

    print(f"{name} spent ${total} on {shirtsText}, {hatsText}, {stickersText}.")

if __name__ == "__main__":
    main()