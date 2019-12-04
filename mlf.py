from sys import stdin

print("#!MLF!#")

for line in stdin:
    line = line.strip()
    line = line.split(" ")
    print(f'"*/{line[0]}.lab"')
    for w in line[1:]:
        print(w)
    print(".")
print("(etc.)")