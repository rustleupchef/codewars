def is_Prime(n: int) -> bool:
    if n <= 1: return False

    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

num = int(input())

print("The number is a prime." if is_Prime(num) else "The number is NOT a prime.")