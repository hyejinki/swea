# 조건문을 이용한 문자열 슬라이싱

# 문자열을 전달 받아 해당 문자열의 정중앙 문자를 출력하시오.
# 단, 문자열의 길이가 짝수일 경우에는 정중앙 문자 2개를 출력하라.
import math
string = input()
n = len(string)
# 문자열 길이가 짝수라면
if n % 2 == 0:
    n1 = int(n / 2 - 1)
    n2 = int(n / 2 + 1)
    print(string[n1:n2])
# 홀수라면
else:
    n = math.trunc(n / 2)
    print(string[n])

