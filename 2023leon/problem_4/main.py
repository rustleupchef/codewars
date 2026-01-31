#Problem 4 solution
import re
def main():
    match = re.match(r'(?P<number>\d+)(?P<string>\w+)', input())
    if match is None:
        print('Error: invalid input')
        return
    times = int(match.group('number'))
    string = match.group('string')
    print(string*times)
if __name__ == '__main__':
    main()