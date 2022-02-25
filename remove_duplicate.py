# remove duplicates
n = int(input())
a = [input(i) for i in range(n)][:n]
dup = []
for char in a:
    if char not in dup:
        dup.append(char)
print(*dup)