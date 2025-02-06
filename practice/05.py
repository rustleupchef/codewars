sep = input()
string = input()
result: str = ""

string = string.split(sep)
string.reverse()

for part in string:
    result += f"{part}{sep}"

print(result[:-len(sep)])