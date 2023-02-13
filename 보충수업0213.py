# # 1. 배열의 메서드
# stack = []

# def push(item):
#     stack.append(item)

# def pop():
#     if len(stack) == 0:     # 아무것도 없는데 꺼내려고 하면 underflow
#         return
#     else:
#         return stack.pop()

# for i in range(10):
#     push(i)

# print(stack)

# for i in range(10):
#     print(pop(), end= " ")


# # 2. 배열을 이용해서 직접 구현
# stack = [0]*10

# def my_push():
#     global top

#     if top == -1:
#         print('')
#         return
#     else:
#         top += 1
#         return stack[top]


# def my_pop():
#     global top

#     if top == -1:
#         print('언더플로우')
#         return
#     else:
#         top -= 1
#         return stack[top+1]

# for i in range(10):
#     my_push(i)

# print(stack)

# for i in range(10):
#     print(my_pop(), end='')


# 파스칼의 삼각형


# # 점화식
# # 첫 번째 열, 마지막 열은 다 1이다. 
# # a21 = a10 + a11
# # a31 = a20 + a21
# # arc = a(r-1)(c-1) + a(r-1)c

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     print(f'#{tc}')
#     # 파스칼의 삼각형 구하기
#     tri = [[0] * r for r in range(1, N+1)]


#     # 한줄씩 구하면서 출력
#     # 이전 행에서 사용했던 결과를 이용해서 현재 행을 구하기
#     for r in range(N):
#         for c in range(r + 1):
#             if c == 0:                  # 맨 왼쪽 열
#                 tri[r][c] = 1
#             elif r == c:                # 대각선
#                 tri[r][c] = 1
#             else:
#                 tri[r][c] = tri[r-1][c-1] + tri[r-1][c]
        
#         print(*tri[r])



# 스택으로 풀기
T = int(input())

for tc in range(1, T+1):
    n = int(input())

    # 첫번째 줄
    tri = [1]
    print(f'{tc}')
    print(*tri)
    # 두 번째 줄부터 스택을 사용해서 삼각형 만들기
    for i in range(n - 1):
        # 현재줄의 맨처음과 끝에 있는 1은 더할 게 없으니 0으로 채워준다.
        stack = [0] + tri + [0]
        tri = [] # 해당 줄에서 사용할 숫자를 저장할 리스트

        # pop()을 하면 최근에 사용했던 값을 가져올 수 있다.
        num = stack.pop()   # 자신의 오른쪽 위 숫자 가져오기

        while stack:
            num2 = stack.pop()      #왼쪽 위 숫자 가져오기
            tri.append(num + num2) 

            num = num2  # 자신의 오른쪽 숫자를 왼쪽 숫자로 바꿔준다.

        print(*tri)      