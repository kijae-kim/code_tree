N, K = map(int, input().split())
num = [int(input()) for _ in range(N)]

# 폭발한 폭탄의 인덱스를 저장할 세트 (중복 방지)
exploded_indices = set()

# 모든 폭탄 쌍을 비교하여 폭발 조건 확인
for i in range(N):
    bmb = num[i]
    for j in range(i + 1, N):
        if abs(i - j) <= K and bmb == num[j]:
            exploded_indices.add(i)
            exploded_indices.add(j)

# 폭발한 폭탄들을 정수별로 셉니다.
cnt_dict = {}
for idx in exploded_indices:
    val = num[idx]
    cnt_dict[val] = cnt_dict.get(val, 0) + 1

# 폭발한 폭탄이 하나도 없는 경우 0을 출력합니다.
if not cnt_dict:
    print(0)
else:
    # 가장 많이 폭발한 횟수를 찾습니다.
    max_cnt = max(cnt_dict.values())
    
    # 가장 많이 폭발한 정수들을 모읍니다.
    candidates = [val for val, cnt in cnt_dict.items() if cnt == max_cnt]
    
    # 가장 많이 폭발한 정수 중 가장 큰 값을 출력합니다.
    print(max(candidates))