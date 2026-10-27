N = int(input())

# Please write your code here.
def num(n):
    if n == 0:
        return
    num(n-1)
    print(n, end=" ")

def num_2(n):
    global N

    if n == 0:
        return
        
    print(n, end=" ")
    num_2(n-1)

num(N)
print()
num_2(N)