# 튜플의 특징과 문자열 반복에 대한..

# 두 개의 정수 n과 m이 주어졌을 때, 가로의 길이가 n, 세로의 길이가 m인
# 직사각형 형태를 별(*) 문자를 이용하여 출력하시오

m = 5
n = 4
list_star = []

for j in range(n):
    list_star.append('*')
for i in range(m):    
    print(*list_star)
