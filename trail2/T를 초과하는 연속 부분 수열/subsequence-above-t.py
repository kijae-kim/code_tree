n, t = map(int, input().split())
arr = list(map(int, input().split()))

# num > t
# max_length(arr)

ans = 0
cnt = 0

# 수열을 순회하며 T보다 큰 연속된 숫자의 최대 길이 구하기
for x in arr:
    if x > t:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)