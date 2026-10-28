n = int(input())
arr = list(map(int, input().split()))

# 순서대로 정수를 읽다가
# 홀수번째 원소가 주어질 때 마다 지금까지 입력 받은 값의 중앙값을 출력해라.


for i in range(0, n, 2):
    tmp = arr[:i+1]
    tmp.sort()
    print(tmp[i//2], end=" ")