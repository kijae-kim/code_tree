n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.

MIN = float("inf")
# 원소 하나를 골라 그 값을 2배로 만든다.
for i in range(n):
    arr[i] = arr[i]*2
    # 그 다음 원소 하나를 골라 제거한다.
        # 이때, 제거할 원소는 앞에서 2배로 만든 원소와 같아도 됨.
    for j in range(n):
        tmp = arr.copy()
        a = arr[j]
        tmp.pop(j)
        # 남은 N-1개의 원소는 원래 순서를 그대로 유지
        # 점수는 인접한 두 원소마다 차의 절대값을 구해 모두 더한 값
        # 점수가 가장 작아지도록 두 원소를 고른다.
        SUM = 0
        for k in range(n-2):
            diff = abs(tmp[k] - tmp[k+1])
            SUM += diff

        MIN = min(MIN, SUM)
    # 복구
    arr[i] = arr[i]//2

print(MIN)