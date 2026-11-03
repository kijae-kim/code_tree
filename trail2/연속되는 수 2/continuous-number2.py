n = int(input())
arr = [int(input()) for _ in range(n)]

MAX = -float('inf')

val = -1
cnt = 1

for i in range(n):
    x = arr[i]
    # 연속된 값이 아닐 경우
    if val != x:
        MAX = max(MAX, cnt)
        val = x
        cnt = 1
    # 연속된 값일 경우
    else:
        cnt += 1
        if i == n-1:
            MAX = max(MAX, cnt)

print(MAX)