n = int(input())
arr = list(map(int, input().split()))


# 유클리드 호제법으로 최대공약수(GCD) 직접 구현
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


# 최소공배수(LCM) 구하기
def lcm(a, b):
    return (a * b) // gcd(a, b)


# 작성하시던 재귀 방식 활용
def basu(i, current_lcm):
    if i == n:
        return current_lcm
    next_lcm = lcm(current_lcm, arr[i])
    return basu(i + 1, next_lcm)


# 첫 번째 원소를 초기값으로 시작
ans = basu(1, arr[0])
print(ans)