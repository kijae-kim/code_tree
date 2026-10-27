n = int(input())

def star(i):
    global n

    if i == 0:
        return
    star(i - 1)
    print('*' * i)

star(n)