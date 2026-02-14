#Problem 17 solution
def main():
    text = ""
    while True:
        line = input()
        if line == ";;;":
            break
        text += line + " "
    text = text.replace(',', " ")
    emails = sorted(list(set([line.lower() for line in text.split()])))
    for email in emails: print(f"{email};")



if __name__ == "__main__":
    main()