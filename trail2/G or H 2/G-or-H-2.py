n = int(input())
people = [tuple(input().split()) for _ in range(n)]


# 오직 H 또는 G로만 이루어져 있거나.
# G와 H가 정확히 같은 개수만큼 나오도록 사진을 찎어야함
# 이때 가능한 사진의 최대 크기를 구해라
# 사진의 크기 : 사진에 찍힌 사람 중 양쪽 끝에 있는 두 사람 사이의 거리

def distance(pos):
    if len(pos) == 1:
        return 0
    else:
        pos = sorted(pos)
        return pos[-1] - pos[0]

# 정렬
sorted_people = sorted(people, key=lambda x: int(x[0]))

if len(sorted_people) <= 1:
    print(0)

else:
    ans = 0

    pos = [int(p[0]) for p in sorted_people]
    alpha = [p[1] for p in sorted_people]

    for i in range(n):
        for j in range(i + 1, n + 1):
            G = 0
            H = 0
            tmp = alpha[i:j]

            for t in range(len(tmp)):
                if tmp[t] == 'G':
                    G += 1
                elif tmp[t] == 'H':
                    H += 1
            # G만 있거나 H만 있거나
            # 거리 계산
            if G > 0 and H == 0:
                dis = distance(pos[i:j])
                ans = max(ans, dis)
            elif H > 0 and G == 0:
                dis = distance(pos[i:j])
                ans = max(ans, dis)
            elif G > 0 and H > 0 and G == H:
                dis = distance(pos[i:j])
                ans = max(ans, dis)
    print(ans)