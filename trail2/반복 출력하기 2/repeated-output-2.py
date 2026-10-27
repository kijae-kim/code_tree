n = int(input())

# Please write your code here.
def world(n):
    if n == 0:
        return
    print("HelloWorld")
    world(n-1)

world(n)