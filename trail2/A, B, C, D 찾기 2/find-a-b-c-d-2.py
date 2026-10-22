nums = list(map(int, input().split()))

nums = sorted(nums)
# Please write your code here.
# 정렬해서 앞의 4개를 구하면 되는거 아닌가
# 1부터 40까지 가능한 모든 A, B, C, D 조합을 탐색합니다.
for a in range(1, 41):
    for b in range(a, 41):
        for c in range(b, 41):
            for d in range(c, 41):
                # 현재 A, B, C, D로 만들 수 있는 15가지 조합의 합
                candidate = [
                    a, b, c, d,
                    a + b, b + c, c + d, d + a,
                    a + c, b + d,
                    a + b + c, a + b + d, a + c + d, b + c + d,
                    a + b + c + d
                ]
                    
                # 만든 조합을 정렬한 결과가 입력받은 15개와 정확히 일치한다면 정답!
                if sorted(candidate) == nums:
                    print(a, b, c, d)