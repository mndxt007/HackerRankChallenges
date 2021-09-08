from collections import Counter

numwords = int(input())

words = [[] for i in range(numwords)]

for i in range(numwords):
    words[i]=input()

counts = Counter(words)

print(len(counts.values()))
print(*counts.values())

