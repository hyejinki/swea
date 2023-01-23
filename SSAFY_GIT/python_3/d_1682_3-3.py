# 딕셔너리로 구성된 리스트의 활용
# 딕셔너리로 이루어진 list를 전달 받아 모든 딕셔너리의 'age' key에 해당하는 value들의 합을 구하시오
infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

# 리스트의 크기 == 딕셔너리 갯수
# infos[i] 돌려가면서 합을 구하면 되겠다.
lis_value = []
n = len(infos)
for i in range(n):
    lis_value.append(infos[i]['age'])

print(sum(lis_value))
