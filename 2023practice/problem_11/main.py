#Problem 11 solution
def main():
    students = int(input())

    fulls = int(students/4)
    partials = (students - students % 4)
    
    if partials > 0:
        if fulls == 1:
            print(f"1 full car, 1 parital car")
        else:
            print(f"{fulls} full cars, 1 partial car")
    else:
        if fulls == 1:
            print(f"1 full car")
        else:
            print(f"{fulls} full cars")

if __name__ == "__main__":
    main()