N = int(input())
arr = [int(input()) for _ in range(N)]

MAX = -float('inf')
y = arr[0]
cnt = 1

if N > 1:
    for i in range(1, N):
        x = arr[i]
        if y > 0 and x > 0:
            cnt += 1
        elif y < 0 and x < 0:
            cnt += 1
        else:
            y = x
            MAX = max(MAX, cnt)
            cnt = 1
        if i == N-1:
            MAX = max(MAX, cnt)
    
    print(MAX)
else:
    print(1)

