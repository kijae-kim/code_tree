N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# 학생 N명
# 벌칙 M번 입력
# K번 걸리면 벌금

ans = -1

checked = [0] * (N+1)

for i in range(M):
    idx = student[i]
    checked[idx] += 1
    if checked[idx] >= K:
        ans = idx
        break

print(ans)