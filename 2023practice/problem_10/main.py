#Problem 10 solution
from datetime import datetime, timedelta

def main():
    start = input()
    stop = input()
    name = input()

    start_date = datetime.strptime(start, "%Y-%m-%d")
    stop_date = datetime.strptime(stop, "%Y-%m-%d")

    months = (stop_date.year - start_date.year) * 12 + stop_date.month - start_date.month
    
    print(f"{name} is {int(months) - 1} months old")

if __name__ == "__main__":
    main()