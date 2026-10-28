n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]


tmp = []

for char in str:
    if char.startswith(t):
        tmp.append(char)

tmp.sort()

print(tmp[k-1])