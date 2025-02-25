num = int(input())

n1 = str(num)
n2 = str(num ** 2)

if n2[-len(n1):] == n1:
    print("Automorphic!!")
else:
    print("No automorphic :(")