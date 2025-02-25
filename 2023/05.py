num = int(input())
moons=["Naiad","Thalassa", "Despina", "Galatea", "Larissa", "Hippocamp","Proteus", "Triton", "Nereid", "Halimede", "Sao", "Laomedeia", "Psamathe","Neso"];

if num > 14 or num < 1:
    print("ERROR")
else:
    print(moons[num - 1])