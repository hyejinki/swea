# 산술연산자를 활용한 근의 공식만들기

# 이차방정식의 근의 공식
# 이차 방정식을 작성하고, 이차방정식의 근을 튜플 형식으로 출력(소수점 4번째 자리에서 반올림)
a = 3
b = 6
c = - 5

root_formula_p = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
root_formula_n = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
ans = (round(root_formula_p, 3), round(root_formula_n, 3))
print(ans)