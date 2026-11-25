# 킹, 퀸, 룩, 비숍, 나이트, 폰
now_list = list(map(int, input().split()))

# 최대 16개의 피스를 사용
# 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개

# 출력
# 몇개를 더해야 올바른 체스 세트가 되는지

goal = [1, 1, 2, 2, 2, 8]

ans = [0] * 6

for i in range(6):
    # 현재 개수가 목표 개수와 다르면?
    # 현재 개수가 목표 개수보다 클 때
    if now_list[i] > goal[i]:
        ans[i] = goal[i] - now_list[i]
    # 현재 개수가 목표 개수보다 작을 때
    elif now_list[i] < goal[i]:
        ans[i] = goal[i] - now_list[i]
    # 같으면?
    else:
        ans[i] = 0

print(*ans)