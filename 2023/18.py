num = int(input())
temp = num
def isPalindrome(number: int) -> bool:
    number = str(number)
    if number == number[::-1]:
        return True
    return False
for i in range(temp):
        temp += int(str(temp)[::-1])
        if isPalindrome(temp):
            print(temp)
            break
else:
    print(f"{num} is not a lychel number")
