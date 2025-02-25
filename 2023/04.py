text = input()
num = ""
for i in range(len(text)):
    if not text[i].isdecimal():
        print(text[i:] * int(num))
        break
    num += text[i]
