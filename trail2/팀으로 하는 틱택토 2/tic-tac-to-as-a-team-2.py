N = 3
inp = [input() for _ in range(3)]

# 두 명이 한 팀을 이룬다.
# 가로 3줄, 세로 3줄, 좌상-우하 대각선 1 + 우상-좌하 대각선 1
# 후보
hubos = []

row_line = []
col_line = []
# 가로 집합을 먼저 만들어 볼까

left = set()
right = set()

for i in range(N):
    row = set()
    col = set()

    for j in range(N):
        row.add(inp[i][j])  # 가로
        col.add(inp[j][i])  # 세로

    left.add(inp[i][i])
    right.add(inp[i][N-1-i])

    hubos.append(row)
    hubos.append(col)

hubos.append(left)
hubos.append(right)

tmp = []
unique_teams = set()  # 중복 팀 저장을 위한 집합

for hubo in hubos:
    # 정확히 2개의 문자로 이루어진 라인인 경우
    if len(hubo) == 2:
        team = tuple(sorted(hubo))
        
        if team not in unique_teams:
            unique_teams.add(team)
            tmp.append(hubo)

print(len(tmp))