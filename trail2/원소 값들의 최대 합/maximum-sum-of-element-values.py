n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))

max_total = -float("inf")

# 1부터 N까지의 모든 위치에서 시작할 때의 결과 계산
for start_idx in range(1, n + 1):
    current_sum = 0
    curr = start_idx

  # m번 이동
    for _ in range(m):
        val = arr[curr]
        current_sum += val
        curr = val  # 다음 위치로 갱신

    if current_sum > max_total:
        max_total = current_sum

print(max_total)