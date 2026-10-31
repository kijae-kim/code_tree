n = int(input())
sequence = list(map(int, input().split()))

# 1. (값, 원래 인덱스) 형태로 묶어서 정렬
indexed_sequence = sorted([(val, idx) for idx, val in enumerate(sequence)])

# 2. 정렬된 순서대로 원래 인덱스 위치에 1부터 시작하는 순위 기록
ans = [0] * n
for rank, (val, original_idx) in enumerate(indexed_sequence, start=1):
  ans[original_idx] = rank

print(*ans)