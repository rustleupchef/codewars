#Problem 15 solution
import datetime

def main():
    months = ["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]
    weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

    dow, month, day = input().split()
    dow = weekdays.index(dow)
    month = months.index(month) + 1
    day = int(day)
    start, end = [int(x) for x in input().split("-")]

    for i in range(start, end):
        try:
            if datetime.date(year=i, month=month, day=day).weekday() == dow:
                print(i)
        except Exception as e:
            pass


if __name__ == "__main__":
    main()