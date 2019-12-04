from sys import stdin
lines = []

for line in stdin:
    line = line.strip()
    lines.append(line)

lines.sort()
for l in lines:
    print(l)