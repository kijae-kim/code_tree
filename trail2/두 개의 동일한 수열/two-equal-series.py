n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A.sort()
B.sort()

same = False
for i in range(n):
    if A[i] == B[i]:
        same = True
    else:
        same = False
        break
    
if same:
    print('Yes')
else:
    print('No')