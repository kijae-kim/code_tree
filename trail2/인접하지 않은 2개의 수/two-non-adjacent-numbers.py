# 첫 번째 줄에서 N을 읽습니다.
N = int(input())
# 두 번째 줄에서 N개의 정수를 리스트로 읽습니다.
A = list(map(int, input().split()))

max_sum = -1

for i in range(N):
    for j in range(i + 2, N):
        current_sum = A[i] + A[j]
        if current_sum > max_sum:
            max_sum = current_sum

print(max_sum)