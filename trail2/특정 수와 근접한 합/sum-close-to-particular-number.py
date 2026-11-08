# 첫 번째 줄에서 N과 S를 입력받습니다.
line1 = input().split()
N = int(line1[0])
S = int(line1[1])

# 두 번째 줄에서 N개의 수를 입력받습니다.
A = list(map(int, input().split()))

# 전체 수의 합을 미리 구합니다.
total_sum = sum(A)
min_diff = float("inf")  # 최솟값을 저장하기 위해 무한대로 초기화

# 서로 다른 두 인덱스 i, j를 골라 2개의 수를 제외합니다.
for i in range(N):
    for j in range(i + 1, N):
        # 제외하고 남은 수들의 합 T
        T = total_sum - A[i] - A[j]

        # S와의 차이의 절댓값 계산
        diff = abs(T - S)

        # 최솟값 갱신
        if diff < min_diff:
            min_diff = diff

print(min_diff)