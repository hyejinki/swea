# def f(i, k):        # bit[i]를 결정하는 함수
#     if i == k:      # bit의 모든 원소 결정
#         print(*bit)
#     else:
#         bit[i] = 0
#         f(i + 1, k)
#         bit[i] = 1
#         f(i + 1, k)
# A = [7, 2, 5, 4, 3]
# N = len(A)
#
# bit = [0] * N   # bit[i] A[i]원소가 부분집합에 포함되는지를 표시함
# f(0, N)

A = [7, 2, 5, 4, 3]
n = len(A)
new = []
for i in range(0, (1<<n)):
    for j in range(0, n):
        if i & (1<<j):
            print(A[j], end='')
    print()

