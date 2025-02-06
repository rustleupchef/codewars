from datetime import datetime, timedelta

signal = input()
start = input()
stop = input()

start_date = datetime.strptime(start, "%Y-%m-%d")
temp_date = start_date
stop_date = datetime.strptime(stop, "%Y-%m-%d")

codes = []
funds = 0.0

while True:
    
    current = str(temp_date.date())
    with open(f"{current}.txt", "r") as file:
        lines = file.read().split('\n')
        file.close()
    
    for line in lines:
        line = line.split(',')
        if line[-1] != signal: continue

        funds += float(line[-2])
        codes.append(line[2])
        
    temp_date += timedelta(days=1)
    if current == str(stop_date.date()):
        break

for code in codes: print(code)
print(f"Funds Found: {funds}")