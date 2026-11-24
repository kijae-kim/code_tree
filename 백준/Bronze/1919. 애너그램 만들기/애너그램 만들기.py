A = input()
B = input()

# 출력
# 애너그램 관계에 있도록 만들기 위해 제거해야하는 최소 개수
# 애너그램으로 만들려면 A에 있는 문자의 수와 B의 문자 수가 같으면됨!

# 애너그램 관계에 있는지 확인
    # 맞으면 cnt 출력
    # 아니면?
        # 몇번째 문자를 빼야할지 선정

dict_a = {}
dict_b = {}

for ch in A:
    dict_a[ch] = dict_a.get(ch, 0) + 1

for ch in B:
    dict_b[ch] = dict_b.get(ch, 0) + 1

removed = 0
#
for ch in set(dict_a.keys()) | set(dict_b.keys()):
    removed += abs(dict_a.get(ch, 0) - dict_b.get(ch, 0))

print(removed)