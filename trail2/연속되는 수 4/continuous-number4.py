n = int(input())
arr = [int(input()) for _ in range(n)]

ans = 0

if n > 1:
    cnt = 1

    for i in range(n-1):
        a1 = arr[i]
        a2 = arr[i+1]
        if a1 < a2:
            cnt += 1
        elif a1 >= a2:
            ans = max(ans, cnt)
            cnt = 1
        if i == n-2:
            ans = max(ans, cnt)
    print(ans)
else:
    print(1)
