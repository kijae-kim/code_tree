N = int(input())

# 홀수인 경우 1부터 N까지의 홀수 합
# 짝수인 경우 2부터 N까지의 짝수 합

def odd_even(n):
    if n == 2:
        return 2
    if n == 1:
        return 1

    if n % 2 == 0:
        return odd_even(n-2) + n
    else:
        return odd_even(n-2) + n

print(odd_even(N))