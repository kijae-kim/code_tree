binary = input()
L = len(binary)
tmp = binary[::-1]

ans = 0

for i in range(L-1, -1, -1):
    x = int(tmp[i])
    num = (2**i) * x
    ans += num

print(ans)