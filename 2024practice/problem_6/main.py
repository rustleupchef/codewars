#Problem 6 solution
def main():
    lines = int(input())

    people = []
    for i in range(lines):
        person = input().split()
        people.append(person)
    
    for person in people:
        name = person[0]
        year = int(person[1])
        month = int(person[2])
        month += year * 12
        print(f"{name} {25 * 12 - month}")

if __name__ == "__main__":
    main()