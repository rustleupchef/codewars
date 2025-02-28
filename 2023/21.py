payments:list[str] = []
while True:
    payment:str = input()
    if payment == ".":
        break
    payment = payment.replace(" ", "")
    payment = payment.split(":")
    if len(payment) > 1:
        try:
            payments.append(int(payment[1]))
        except:
            print("ERROR")
            payments.clear()
            break
    else:
        print("ERROR")
        payments.clear()
        break

if len(payments) > 0:
    payments = [int(money) for money in payments]
    for money in payments:
        if money > 50000:
            print("AMOUNT EXCEEDED")
            break
    else:
        if sum(payments) > 100000:
            print("AMOUNT EXCEEDED")
        else:
            print(f"OK: {sum(payments)}")