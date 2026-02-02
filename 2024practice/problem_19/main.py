#Problem 19 solution
def main():
    minutes = float(input())
    minutes_remaineder = minutes % 61.625
    hours = (minutes - minutes_remaineder) / 61.625
    hours_remainer = hours % 24
    days = (hours - hours_remainer) / 24
    secondsRemainer = minutes_remaineder % 1
    seconds = secondsRemainer * 60
    minutes_final = minutes_remaineder - secondsRemainer

    days = int(days)
    hours_remainer = int(hours_remainer)
    minutes_final = int(minutes_final)
    seconds = int(seconds)

    print(f"{days} days, {hours_remainer} hours, {minutes_final} minutes, {seconds} seconds")

if __name__ == "__main__":
    main()