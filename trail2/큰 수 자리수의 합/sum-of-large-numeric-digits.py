a, b, c = map(int, input().split())

# 세 자리로 이루어진 정수 3개가 주어지면
    # 곱한 후
        # 각 자리 수의 합을 구하라

val = a*b*c

def f(val):
    if val < 10:
        return val
    
    return f(val//10) + val%10

print(f(val))