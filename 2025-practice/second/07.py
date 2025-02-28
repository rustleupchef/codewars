records = []
for i in range(5):
    records.append(input())

dictionary = {}

for record in records:
    nums = [int(num) for num in record.split()[:-1]]
    name = record.split()[-1]
    total = 0
    for i in range(0, len(nums), 2):
        total += abs(nums[i] - nums[i + 1])
    dictionary[total] = name

keys = list(dictionary.keys())
keys.sort()
keys.reverse()

for key in keys:
    print(key, dictionary[key])