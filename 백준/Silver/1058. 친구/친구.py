N = int(input())
grid = [input() for _ in range(N)]

ans = 0

node = []

# 친구인지 아닌지를 먼저 판단
for i in range(N):
    f = []
    for j in range(N):
        if grid[i][j] == 'Y':
            f.append(j)
    node.append(f)

for i in range(N):
    friend = node[i]

    friend_list = set()
    # 직접 친구
    for df in friend:
        friend_list.add(df)
        # 간접 친구
        for ff in node[df]:
            friend_list.add(ff)
    friend_list.discard(i)
    ans = max(ans, len(friend_list))

print(ans)