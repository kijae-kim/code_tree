N, B = map(int, input().split())

result = []
while N > 0:
    remainder = N % B   # B로 나눈 나머지
    result.append(str(remainder))
    N //= B            # N을 B로 나눈 몫으로 갱신

# 나머지를 역순으로 뒤집어서 출력
print(''.join(result[::-1]))