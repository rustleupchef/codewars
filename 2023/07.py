num = int(input())
cDniLetters = "AGMYFPDXBNJZSQVHLCKE"
print(cDniLetters[(num % 23) % 23])