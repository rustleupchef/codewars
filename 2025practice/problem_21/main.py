#Problem 21 solution

import math

def truncate_dec(number, decimals):
    return math.trunc(number * (10 ** decimals)) / (10 ** decimals)

def main():
    files = 0.0

    while True:
        line = input()
        if line == 'STOP':
            break
        pairs = line.split()
        files += float(pairs[-1]) * float(pairs[-2])
    
    print(f"Files {truncate_dec(files, 2):.2f} MiB")
    print(f"Files {truncate_dec(files * (2 ** 20/10**6), 2):.2f} MB")
    print(f"Files {truncate_dec((files + 700) * (2 ** 20/10**6), 2):.2f} MB")

    toBeat = truncate_dec((files + 700) * (2 ** 20/10**6), 2)

    phones = {
        "hPhone" : (100, "100 MB"),
        "hPhone1" : (250, "250 MB"),
        "hPhone2" : (500, "500 MB"),
        "hPhone3" : (1000, "1 GB"),
        "hPhone4" : (10_000, "10 GB"),
        "hPhone5" : (50_000, "50 GB"),
        "hPhone6" : (75_000, "75 GB"),
        "hPhone7" : (100_000, "100 GB"),
        "hPhone8" : (150_000, "150 GB"),
        "hPhone9" : (200_000, "200 GB"),
        "hPhoneX" : (500_000, "500 GB"),
        "hPhoneX1" : (1_000_000, "1 TB"),
        "hPhoneX2" : (2_000_000, "2 TB")
    }

    for phone in phones.keys():
        if toBeat <= phones.get(phone)[0]:
            print(f"Need {phone} with {phones.get(phone)[1]} storage")
            break


if __name__ == "__main__":
    main()