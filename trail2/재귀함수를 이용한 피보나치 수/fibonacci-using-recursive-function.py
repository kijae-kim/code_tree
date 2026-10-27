N = int(input())

# 이전 두 항의 합이 그 다음 항이 되는 수열 [피보나치 수열]

def pibo(n):
    if n <= 2:
        return 1
    
    return pibo(n-1) + pibo(n-2)

print(pibo(N))