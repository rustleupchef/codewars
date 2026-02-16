#Problem 3 solution
def main():
    population = int(input())
    capacity = int(input())
    growth = float(input()) + 1
    years = int(input())

    future = int(population * growth * years)
    
    print(f"At current rate of growth there will be {future} ponies in {years} years")
    if future > capacity:
        print(f"Celestia will need to add space for at least {future - capacity} ponies!")
    else:
        print(f"Celestia won't need to add space yet!")


if __name__ == "__main__":
    main()