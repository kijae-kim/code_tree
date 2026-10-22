n = int(input())
seat = input()
    
#  '0'인 빈 자리의 인덱스들을 모두 찾습니다.
empty_spots = []
for i in range(n):
    if seat[i] == '0':
        empty_spots.append(i)
            
max_min_dist = -1
    
#  빈 자리 중에서 2개를 고르는 모든 조합을 탐색합니다.
length = len(empty_spots)
for i in range(length):
    for j in range(i + 1, length):
         # 새로운 자리 배치(리스트)를 만듭니다.
        new_seat = list(seat)
        new_seat[empty_spots[i]] = '1'
        new_seat[empty_spots[j]] = '1'
            
        # 현재 배치에서 사람들이 앉아 있는 위치들을 모읍니다.
        people = []
        for idx in range(n):
            if new_seat[idx] == '1':
                people.append(idx)
            
        # 인접한 사람들 사이의 거리를 구해 최솟값을 찾습니다.
        min_dist = float('inf')
        for p in range(len(people) - 1):
            dist = people[p + 1] - people[p]
            if dist < min_dist:
               min_dist = dist
                    
        # 각 배치마다 구한 '가장 가까운 거리' 중 가장 큰 값을 갱신합니다.
        if min_dist > max_min_dist:
            max_min_dist = min_dist
                
print(max_min_dist)