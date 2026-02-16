#Problem 16 solution

def swap(text, a, b):
    line = ""
    text = text.lower()
    a = a.lower()
    b = b.lower()
    for character in text:
        if character == a:
            line += b
            continue

        if character == b:
            line += a
            continue

        line += character
    
    return line

def main():
    first, second = input().split()

    words = []
    while True:
        line = input()
        if line == "END":
            break
        words.append(line)
    
    transformed = {}
    for word in words:
        transformed[word] = swap(word, first, second)
    
    words = sorted(words, key=transformed.get)
    for word in words:
        print(word)

if __name__ == "__main__":
    main()