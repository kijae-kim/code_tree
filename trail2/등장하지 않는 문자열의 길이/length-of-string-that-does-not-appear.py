N = int(input())
S = input()

# 길이가 L인 연속 부분문자열에 중복이 있는지 확인하는 함수
def check(L):
    seen = set()
    for i in range(N - L + 1):
        sub = S[i:i + L]
        if sub in seen:
            return False  # 중복이 존재함
        seen.add(sub)
    return True  # 모두 서로 다름

start = 1
end = N
ans = N  # 최솟값을 찾아야 하므로 초기값은 N으로 설정

while start <= end:
    mid = (start + end) // 2  # mid는 검사할 부분문자열의 길이(L)
    
    if check(mid):  # 중복이 없다면 조건을 만족하므로, 더 짧은 길이도 가능한지 탐색
        ans = mid
        end = mid - 1
    else:  # 중복이 발생했다면 길이가 더 길어져야 하므로 왼쪽 범위를 조정
        start = mid + 1

print(ans)