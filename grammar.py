import sys

words_set = set()


for line in sys.stdin:
    words = ["/START"]
    words += line.strip().split() + ["/END"]
    print(words)