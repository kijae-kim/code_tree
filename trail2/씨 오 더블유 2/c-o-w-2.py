N = int(input())
S = input().strip().lower()  # 입력받은 문자열을 모두 소문자로 변환

count = 0

# 1 <= i < j < k <= N 조건을 만족하는 세 위치를 탐색합니다.
for i in range(N):
    if S[i] == "c":
        for j in range(i + 1, N):
            if S[j] == "o":
                for k in range(j + 1, N):
                    if S[k] == "w":
                        count += 1

print(count)