n = int(input())
nums = list(map(int, input().split()))
nums.sort()

ans = 0

for i in range(n):
    current = nums[i] + nums[2*n -1 -i]
    if current > ans:
        ans = current

print(ans)