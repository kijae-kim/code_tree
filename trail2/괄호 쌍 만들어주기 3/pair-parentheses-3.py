A = input()
ans = 0
open_count = 0  # 현재 위치 전까지 나온 여는 감싸기 개수

for char in A:
    if char == '(':
        open_count += 1
    elif char == ')':
        # 현재 닫는 괄호 앞에 나온 여는 괄호의 개수만큼 쌍을 만들 수 있음
        ans += open_count

print(ans)