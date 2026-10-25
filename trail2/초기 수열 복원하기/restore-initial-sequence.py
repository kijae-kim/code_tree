n = int(input())
S = list(map(int, input().split())) if n >= 2 else []

for a0 in range(1, n + 1):
    hubo = [a0] # A_0 결정
    seen = {a0} # 숫자가 중복으로 쓰이는지 확인하기 위한 집합
    possible = True
    
    # S_i = A_i + A_{i+1} 이므로 A_{i+1} = S_i - A_i
    for i in range(n - 1):
        next_a = S[i] - hubo[-1]
        
        # 1. 값이 1부터 n 사이의 범위를 벗어나거나
        # 2. 이미 사용된 숫자라면 잘못된 수열이므로 중단
        if not (1 <= next_a <= n) or next_a in seen:
            possible = False
            break
            
        seen.add(next_a)
        hubo.append(next_a)
    
    # 조건을 모두 만족하는 수열을 찾았다면
    if possible and len(hubo) == n:
        # 문제에서 요구하는 형식(공백으로 구분된 한 줄 출력)으로 출력
        print(*hubo)
        # a0을 1부터 차례대로 탐색하므로, 처음 찾은 것이 '사전순으로 가장 앞선 수열'입니다.
        break