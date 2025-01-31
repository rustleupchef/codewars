def one() -> None:
    print("You are not prepared for what is to come.")

def two(name: str) -> str:
    return f"Your real strenght comes from being the best {name} you can be!"

def three(nums: str) -> int:
    x = nums.split()[0]
    y = nums.split()[0]
    return x / y * (y + y)

def three(nums: str) -> str:
    nums = nums.split('\n')
    minutesAgo = ""
    for num in nums:
        s = 's' if num == "1" else ''
        minutesAgo += f"You, {num} minute{s} ago\n";
    return minutesAgo

def four(sketch: str) -> str:
    sketch.replace("\n", "")
    sketch.replace("`", "\n")
    return sketch[1:len(sketch)]

def five(codes: str) -> str:
    sample = ""
    for code in codes.split():
        sample += chr(int(code))
    return sample

def six(people: str) -> str:
    people = people.split("\n")[1:len(people.split("\n"))]
    result = ""
    for person in people:
        stats = person.split(" ")
        age = int(stats[1]) * 12 + int(stats[2])
        result += f"{stats[0]} {(25 * 12) - age}\n"
    return result[0:-1]

def seven(string: str) -> str:
    output = ""
    currentchar = string[0]
    counter = 1
    for i in range(1, len(string)):
        if currentchar == string[i]:
            counter += 1
        else:
            if counter == 4: output += str(currentchar)
            currentchar = string[i]
            counter = 1
    return output

def eight(license: str) -> str:
    newlisence = ""

    nums = []
    letters = []
    id = []

    for i in range(len(license)):
        if license[i].isdecimal():
            nums.append(license[i])
            id.append(True)
        else:
            letters.append(license[i])
            id.append(False)

    nums.sort()
    letters.sort()

    for i in range(len(id) - 1, -1, -1):
        if id[i]:
            newlisence = nums.pop() + newlisence
        else:
            newlisence = letters.pop() + newlisence
    
    return newlisence

def nine(radio: str) -> str:
    radio.replace("STOP", "")
    lastIndex = 0
    stutterless = str(radio[lastIndex])
    for i in range(1, len(radio)):
        if not radio[i].isalpha:
            lastIndex = i
            stutterless += radio[i]
        if radio[i] == radio[lastIndex]:
            if i - lastIndex  == 1:
                stutterless += radio[i]
            else:
                lastIndex = i
            continue
        lastIndex = i
        stutterless += radio[i]
    return stutterless

def ten(solve: str) -> str:
    result = ""
    solve = solve.split("\n")[0:-1]
    for equation in solve:
        expressions = equation.split("=")
        x = int(expressions[0].split("+")[0])
        y = int(expressions[0].split("+")[1])
        if (x + y == int(expressions[-1])):
            result += "CORRECT\n"
        else:
            result += f"WRONG: {x}+{y}={x+y}\n"
    return result

def eleven(nums: str) -> str:
    result = ""
    nums = nums.split("\n")[0:-1]
    for num in nums:
        items = num.split()
        result += f"{int(int(items[0]) - (int(items[1]) / 1000))}"
    return  result

def twelve(socks: str) -> str:
    socks = socks.split("\n")[0:-1]
    s = set()

    for sock in socks:
        if sock in s:
            s.remove(sock)
            continue
        s.add(sock)

    sets = ""
    s = list(s)
    if (len(s) < 1):
        return "No lost socks"
    
    for sock in s:
        sets += sock + "\n"
    
    return sets[0:-1]

def thirteen(box: str) -> str:
    (width, length) = (len(box.split("\n")[0]),len(box.split("\n")))
    newBox = ""
    for i in range(length):
        for j in range(width):
            if (i == 0 or i == length - 1) or (j == 0 or j == width - 1):
                newBox += "*"
                continue
            newBox += " "
        newBox += "\n"
    
    newBox = newBox[0:-1]
    if (box == newBox):
        return "Nothing to do"
    
    return newBox

#someone explain me this question
def fourteen(nums: str) -> str:
    cleanNums = ""
    nums = nums.split(" ")
    for i in range(0, len(nums) - 1):
        if len(nums[i]) == 1 and not nums[i][0].isdecimal(): continue
        cleanNums += nums[i] + " "
    cleanNums = cleanNums[0:-1]
    target = float(nums[1].split("=")[1])

def fifteen(formula: str) -> str:
    formula = formula.split(" ")[0]
    subscript = formula

    for i in range(len(formula)):
        if (formula[i].isdecimal()):
            formula = formula.replace(formula[i], " ")
    for i in range(len(subscript)):
        if (subscript[i].isalpha()):
            subscript = subscript.replace(subscript[i], " ")

    return f"{formula}\n{subscript}"

def sixteen(watched: str) -> str:
    watched = watched.split("\n")[0:-1]
    dictionary = dict()

    for watch in watched:
        if watch in dictionary:
            dictionary[watch] = dictionary[watch] + 1
            continue
        dictionary[watch] = 1
    
    trending_key = max(dictionary, key=dictionary.get)
    trending_value = dictionary[trending_key]
    dictionary.pop(trending_key)
    second_key = max(dictionary, key=dictionary.get)

    return f"Trending: {trending_key} [{trending_value} count]\nSecond Place: {second_key} [{dictionary[second_key]} count]"

def seventeen(excerpt: str) -> str:
    dictionary = dict()
    excerpt = excerpt.split("\n")
    for i in range(1, int(excerpt[0]) + 1):
        items = excerpt[i].split("=")
        options = items[1].split(",")
        options.reverse()
        dictionary[f"<{items[0].upper()}>"] = options

    excerpt = excerpt[int(excerpt[0]) + 1:-1]
    
    for i in range(len(excerpt)):
        for key in dictionary.keys():
            if excerpt[i].find(key) != -1:
                excerpt[i] = excerpt[i].replace(key, dictionary[key].pop(), 1)
    result = ""
    for line in excerpt:
        result += line + "\n"
    return result[0:-1]

def eighteen(graph: str) -> str:
    result = ""
    graph = graph.split('\n')
    variables = graph[-1]

    for i in range(len(variables)):
        if not variables[i].isalpha(): continue
        counter = 0
        j = -3
        while True:
            if len(graph) < j or len(graph[j]) < i: break
            if graph[j][i].upper() == 'X':
                counter += 1
            else:
                break
            j -= 1
        result += f"{variables[i]}: {counter}\n"
    return result[0:-1]

def nineteen(minutes: float) -> str:
    daysRemainder = minutes % (24 * 61.625)
    days = (minutes - daysRemainder) / (24 * 61.625)
    hoursRemainder = daysRemainder % (61.625)
    hours = (daysRemainder - hoursRemainder) / (61.625)
    minutesRemainder = hoursRemainder % 1
    minutes = hoursRemainder - minutesRemainder
    seconds = minutesRemainder * 60
    return f"{days=} {hours=} {minutes=} {seconds=}"

def twenty(text: str) -> str:
    result = ""
    text = text.split('\n')[0:-1]
    for line in text:
        line = line.split(',')
        for i in range(len(line) - 3):
            result += (line[i][1:] if line[i][0] == ' ' else line[i]) + '\n'
        result += f"{line[-3][1:]},{line[-2]}{line[-1]}\n\n"
    return result[:-2]

def twentyone(words: str) -> str:
    result = ""
    words = words.split('\n')[:-1]
    for wordStr in words:
        word = list(wordStr)
        sorted = word[:]
        sorted.sort()
        if word == sorted:
            result += f"{wordStr} SORTED\n"
            continue

        vow = list()
        con = list()

        vowels = ['a', 'i', 'e', 'o', 'u']

        for character in word:
            if character in vowels:
                vow.append(character)
            else:
                con.append(character)
        
        sortedCon = con[:]
        sortedCon.sort()

        if con == sortedCon:
            result += f"{wordStr} CON-SORTED\n"
            continue

        sortedVow = vow[:]
        sortedVow.sort()

        if vow == sortedVow:
            result += f"{wordStr} VOW-SORTED\n"
            continue

        result += f"{wordStr} UNSORTED\n"
    return result

def main() -> str:
    with open("input.txt", 'r') as file:
        text = file.read()
        file.close()
    return twentyone(text)

if __name__ == "__main__":
    print(main())