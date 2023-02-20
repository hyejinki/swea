
# for test_case in range(1, 11):
#     N = int(input())
#     arr = [list(map(int, input().split()))for _ in range(100)]
#     i = 99
#     j = arr[99].index(2)

#     while i >= 0:          # 0행까지
#         if i == 0:
#             break
#         if j >= 1 and arr[i][j - 1]:  # 왼쪽에 있으면
#             while j > 0:
#                 if arr[i-1][j-1]:
#                     i -= 1
#                     j -= 1          # 왼쪽으로
#                     break
#                 else:
#                     j -= 1
#         elif j <= 98 and arr[i][j+1]:       # 오른쪽에 있으면
#             while j < 99:
#                 if arr[i-1][j+1]:
#                     i -= 1
#                     j += 1          # 오른쪽으로
#                     break
#                 else:
#                     j += 1
#         else:
#             arr[i][j] == 0
#             i -= 1                 # 양쪽에 사다리 없으면 위로
#     print(f'#{test_case}', j)

# 피보나치 재귀
# def fibo1(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return fibo1(n -1) + fibo1(n - 2)
    
# print(fibo1(5))

# 피보나치 디피
# def fibo2(n):
    
#     f = [0] * (n+1)
#     f[0] = 1
#     f[1] = 1
#     for i in range(2, n+1):
#         f[i] = f[i - 1] + f[i - 2]

#     return f[n]
# print(fibo2(5))



# fn = [input()]

# stack = [0] * len(fn)
# top = -1
# postfix = ''
# op = {'*':2 , '/' : 2, '+' : 1, '-' : 1}

# for t in fn:
#     if '0' <= t <= '9':
#         postfix += t
#     elif t in op:
#         if top == -1 or op[stack[top]] < op[t]:     # 토큰의 우선순위가 높으면
#             top += 1
#             stack[top] = t
#         else:
#             while top > -1 and op[stack[top]] >= op[t]:
#                 top = -1
#                 postfix += stack[top+1]
#             top += 1
#             stack[top] = t
# while top > -1:
#     top -= 1
#     postfix += stack[top+1]
# print(postfix)


# def f(i, k):  # i : 복사할 인덱스 , k 배열의 크기
#     if i == k:
#         print(B)
#     else:
#         B[i] = A[i]
#         f(i + 1, k)

# A = [10, 20, 30]
# N = len(A)
# B = [0] * N
# f(0, N)


# def f(i, k key):
#     if i == k:
#         return 0
#     elif A[i] == key:
#         return 1
#     else:
#         return f(i+1, k, key)

# A = [7, 2, 5, 3, 8, 9]
# N = len(A)
# key = 3
# print(f(0, N, key))
# key = 6
# print(f(0, N, key))


# q부분집합
def f(i, k):
    if i == k:
        print(bit)
    else:
        bit[i] = 0
        f(i+1, k)
        bit[i] = 0
        f(i+1, k)
    return

A = [2, 3, 7, 9, 8]
N = len(A)
bit = [0]*N
f(0, N)