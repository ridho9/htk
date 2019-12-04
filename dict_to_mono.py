from sys import stdin

monoph = set()

for line in stdin:
    line = line.strip().split(" ")[1:]
    for m in line:
        monoph.add(m)

for c in sorted(list(monoph)):
    print(c)