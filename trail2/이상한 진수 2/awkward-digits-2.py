a = list(input())
changed = False

# 1. 왼쪽부터 탐색하며 가장 먼저 나오는 '0'을 '1'로 변경
for i in range(len(a)):
    if a[i] == '0':
        a[i] = '1'
        changed = True
        break

# 2. 만약 바꾼 적이 없다면 (모든 자리가 '1'인 경우: '1111', '1' 등)
# 값의 감소를 최소화하기 위해 가장 오른쪽 끝자리('1')를 '0'으로 변경
if not changed:
    a[-1] = '0'

print(int("".join(a), 2))