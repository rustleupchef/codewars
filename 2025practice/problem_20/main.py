from datetime import datetime, timedelta

def main():
    start = input()
    day = input()
    stop = input()

    start_date = datetime.strptime(start, "%Y-%m-%d")
    temp_date = start_date
    stop_date = datetime.strptime(stop, "%Y-%m-%d")


    counter = 0
    while True:
        current = str(temp_date.date())
        counter += 1
        temp_date += timedelta(days=1)
        if current == str(stop_date.date()):
            break
    days = ["Mahomesday", "Jonesday", "Kelceday", "McDuffieday", "Humphreyday", "Thuneyday", "Smithday"]
    print(f"{stop} is a {days[(days.index(day) + counter) % len(days) - 1]}")
    if day == 1:
        print("There is one day between the two dates")
    else:
        print(f"There are {counter - 2} days between the two dates")

    

if __name__ == "__main__":
    main()