#Problem 18 solution
import math

def truncate(num, dec):
    return math.trunc(num * (10 ** dec)) / (10 ** dec)

def main():
    schools = []
    for i in range(int(input())):
        name, count = input().split()
        schools.append([name, int(count)])

    totalTc = sum([count for name, count in schools])
    maxTeamNumber  = 100 + totalTc
    maxTc = min(max([count for name, count in schools]), totalTc//2)
    skipVal = math.floor(totalTc/maxTc)
    baseTeamValue = 100
    nextTeamNumber = baseTeamValue

    print(totalTc)
    for name, count in schools:
        counts = []
        for i in range(count):
            nextTeamNumber += skipVal

            if nextTeamNumber > maxTeamNumber:
                baseTeamValue -= 1
                nextTeamNumber = baseTeamValue
                nextTeamNumber += skipVal

            counts.append(nextTeamNumber)

        failure = False
        for i in range(len(counts)):
            for j in range(i + 1, len(counts)):
                if abs(counts[i] - counts[j]) < skipVal:
                    failure = True

        if failure:
            counts.append("FAILURE")
        
        print(f"{name} {count}: {' '.join([str(num) for num in counts])}")


if __name__ == "__main__":
    main()