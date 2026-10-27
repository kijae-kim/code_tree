n = int(input())
arr = list(map(int, input().split()))

# n개 원소 Arr 중 최댓값을 구하라

ans = -float("inf")

def f(n, ans):
    if n == 0:
        return ans
    
    val = arr[n-1]

    return f(n-1, max(ans, val))

print(f(n, ans))