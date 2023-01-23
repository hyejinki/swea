# 복합 자료형인 딕셔너리 작성 및 활용
# 여러 사람의 혈액형(A, B, AB, O)에 대한 정보가 담긴 list를 전달 받아,
# key는 혈액형 종류, value는 사람 수인 dictionary를 만드시오

blood_types = [ 'A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']

# lis_type = ['A', 'B', 'AB', 'O']
# lis_count = [0] * 4
# for i in blood_types:
#     if i == 'A':
#         lis_count[0] += 1
#     elif i == 'B':
#         lis_count[1] += 1
#     elif i == 'AB':
#         lis_count[2] += 1
#     else:
#         lis_count[3] += 1
# dic_blood = dict(zip(lis_type, lis_count))

# print(dic_blood)
n = len(blood_types)
lis_type = ['A', 'B', 'AB', 'O']
lis_count = [0] * 4
for i in range(4):
    for j in blood_types:
        if lis_type[i] == j:
            lis_count[i] += 1
dic_blood = dict(zip(lis_type, lis_count))

print(dic_blood)
