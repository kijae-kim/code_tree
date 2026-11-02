a, b = map(int, input().split())
n = input()

if n == '0':
    print(0)
else:
    decimal = int(n, a)

    ans = []

    while decimal > 0:
        tmp = decimal % b
        ans.append(str(tmp))
        decimal //= b

    print(''.join(ans[::-1]))