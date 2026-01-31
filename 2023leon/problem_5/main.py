#Problem 5 solution
def main():
    nNumero=int(input(""))
    moons=["Naiad","Thalassa", "Despina", "Galatea", "Larissa", "Hippocamp",
    "Proteus", "Triton", "Nereid", "Halimede", "Sao", "Laomedeia",
    "Psamathe","Neso"]
    if (nNumero<1):
        print("ERROR")
    elif (nNumero>14):
        print("ERROR")
    else:
        print(moons[nNumero-1])
if __name__ == "__main__":
    main()