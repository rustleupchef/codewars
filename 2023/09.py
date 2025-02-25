hosts = []

while True:
    host = int(input())
    if host < 0: break
    hosts.append(host)

print(f"The number of hosts is: {len(hosts)}")

avg = 0.0
for host in hosts:
    avg += host

print(f"The average age of hosts is: {avg / float(len(hosts))}")