N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# B를 미리 정렬해 둠
sorted_B = sorted(B)
cnt = 0

# 길이가 M인 연속 부분 수열의 시작 인덱스 i는 0부터 N - M까지 가능
for i in range(N - M + 1):
  hubo_A = A[i : i + M]  # 길이가 M인 연속 부분 수열

  # 부분 수열을 정렬한 결과가 sorted_B와 같으면 아름다운 수열!
  if sorted(hubo_A) == sorted_B:
    cnt += 1

print(cnt)