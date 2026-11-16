n = int(input())
arr = [int(input()) for _ in range(n)]

ans = -1  # carry가 전혀 발생하지 않는 경우가 없으면 -1 출력

for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            first, second, third = arr[i], arr[j], arr[k]
            total = first + second + third  # 미리 합을 저장해 둠

            is_carry = False
            # 세 수 모두 0이 될 때까지 각 자릿수(1의 자리 -> 10의 자리 -> ...) 확인
            while first > 0 or second > 0 or third > 0:
                digit_sum = (first % 10) + (second % 10) + (third % 10)
                if digit_sum >= 10:
                    is_carry = True
                    break

                # 다음 자릿수(10의 자리)를 1의 자리로 끌어내림
                first //= 10
                second //= 10
                third //= 10

            # carry가 한 번도 발생하지 않았다면 최댓값 갱신
            if not is_carry:
                ans = max(ans, total)

print(ans)
