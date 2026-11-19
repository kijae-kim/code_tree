n = int(input())
arr = list(map(int, input().split()))

# 조건을 만족하는 구간이 몇 개인지 세는 프로그램
# l과 r의 쌍 (l,r)이 다르면 원소의 값이 같더라도 서로 다른 구간으로 센다.
cnt = 0

for i in range(n):
  for j in range(i, n):
    SUM = 0
    for k in range(i, j + 1):
      SUM += arr[k]
    AVG = SUM / (j - i + 1)

    # 구간 [i, j] 내에 평균값(AVG)과 같은 원소가 있는지 확인
    if AVG in arr[i : j + 1]:
      cnt += 1

print(cnt)