N = int(input())
H = [int(input()) for _ in range(N)]
# max(H) - min(H) <= 17
# goal : min_price

min_price = float("inf")

# 높이를 조정할 언덕을 먼저 찾는게 우선인듯
# 최소 높이가 될 수 있는 언덕을 먼저 정해
for low in range(101):
    high = low + 17
    current_price = 0
    for h in H:
        if h < low:
            current_price += (low-h)**2
        elif h > high:
            current_price += (high-h)**2
        
    if current_price < min_price:
        min_price = current_price

print(min_price)