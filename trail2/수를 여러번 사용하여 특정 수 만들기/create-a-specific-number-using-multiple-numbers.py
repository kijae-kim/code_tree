A, B, C = map(int, input().split())

# Please write your code here.
# A와  B를 0번 이상 더해서 만들 수 있는 C 이하인 수 중에서 가장 큰 값

MAX = -float("inf")     # C가 최대임

for i in range(C):
    for j in range(C):
        SUM = (A*i) + (B*j)
        if SUM < MAX:
            continue
        if SUM <= C:
            MAX = max(SUM, MAX)

print(MAX)