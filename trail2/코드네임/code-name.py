class User:
    def __init__(self, name, score):
        self.name = name
        self.score = score

MAX_N = 5

users = []
for _ in range(MAX_N):
    codename, score = input().split()
    users.append(User(codename, int(score)))

ans = float('inf')
name = ""

for i in range(MAX_N):
    user = users[i]
    if ans > user.score:
        ans = user.score
        name = user.name

print(name, ans)