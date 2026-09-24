#Problem 13 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    time = [int(value) for value in input().split(":")]
    minutes = time[0]
    seconds = time[1]

    speeds = []
    while True:
        line = input()

        if line == "0.0x":
            break

        speeds.append(float(line[:-1]))

    for speed in speeds:
        total_seconds = minutes * 60 + seconds

        total_seconds /= speed

        seconds_remainder = total_seconds % 60
        m = int((total_seconds - seconds_remainder) // 60)
        s = str(int(seconds_remainder))
        new_time = f"{m}:{'0' * (2 - len(s))}{s}"

        print(f"{minutes}:{'0' * (2 - len(str(seconds)))}{seconds} is {new_time} at {speed}x speed")
    

if __name__ == "__main__":
    main()