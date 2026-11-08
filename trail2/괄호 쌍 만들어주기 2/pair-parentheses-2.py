A = input()
n = len(A)

open_indices = []
for i in range(n - 1):
    if A[i] == "(" and A[i + 1] == "(":
        open_indices.append(i)

close_indices = []
for j in range(n - 1):
    if A[j] == ")" and A[j + 1] == ")":
        close_indices.append(j)

count = 0
for i in open_indices:
    for j in close_indices:
        if i + 2 <= j:
            count += 1

print(count)