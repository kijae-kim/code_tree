from collections import deque
import sys

input = sys.stdin.readline
MAX = 100000

n, k = map(int, input().split())
dist = [-1] * (MAX + 1)

queue = deque([n])
dist[n] = 0

while queue:
    x = queue.popleft()
    if x == k:
        print(dist[x])
        break

    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= MAX and dist[nx] == -1:
            dist[nx] = dist[x] + 1
            queue.append(nx)