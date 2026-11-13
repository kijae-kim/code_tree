N = int(input())
A = list(map(int, input().split()))

# 10마리 소가 위치 1부터 N까지 도열해있다.
# 소의 키는 a_i이며 서로 다른 소의 위치 (i,j,k)일 때
    # i < j < k & ai < aj < ak를 동시에 만족하는
    # i,j,k 조합의 개수를 구해라

# 소의 위치값과 value 값이 중요함
ans = 0
tmp = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if i < j < k and A[i] <= A[j] <= A[k]:
                tmp.append((i,j,k))
                ans += 1

print(ans)