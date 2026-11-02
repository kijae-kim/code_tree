N = input()

# Please write your code here.
demical = int(N, 2)

tmp = demical * 17

ans = bin(tmp)[2:]

print(ans)