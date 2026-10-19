N = int(input())
seat = input()

max_min_dist = -1

# 0인 모든 빈자리에 한 명씩 새로운 사람을 앉혀봅니다.
for i in range(N):
  if seat[i] == '0':
    # 새로운 좌석 상태 생성 (i번째 자리에 '1'을 넣음)
    new_seat = seat[:i] + '1' + seat[i + 1 :]

    # 새로운 상태에서 학생('1')들의 인덱스를 모음
    students = []
    for j in range(N):
      if new_seat[j] == '1':
        students.append(j)

    # 이 배치에서 가장 가까운 두 사람의 거리(최소 거리)를 구함
    min_dist = float('inf')
    for k in range(len(students) - 1):
      dist = students[k + 1] - students[k]
      if dist < min_dist:
        min_dist = dist

    # 가능한 최소 거리들 중 최댓값을 갱신
    if min_dist > max_min_dist:
      max_min_dist = min_dist

print(max_min_dist)