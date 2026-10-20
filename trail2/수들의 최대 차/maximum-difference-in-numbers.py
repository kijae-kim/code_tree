N, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

# N과 최대로 차이날 수 있는 값 K
    # max - min <= K

# output : 원소의 최대 개수
# 정렬
arr = sorted(arr)
hubo = []

for k in range(N):
    # 앞에서 시작
    min_num = arr[k]
    max_num = 0
    cnt = 1

    for i in range(k+1, N):
        max_num = max(max_num, arr[i])
        if max_num <= K + min_num:
            cnt += 1
    
    hubo.append(cnt)

print(max(hubo))