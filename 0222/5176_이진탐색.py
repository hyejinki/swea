def inorder_t(i, N):           # 중위순회
    if i <= N:
        inorder_t(2*i, N)       # 왼
        stack.append(i)
        inorder_t(2*i+1, N)     # 오
    else:
        return

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    stack = []              # 탐색 순서대로
    inorder_t(1, N)

    for i in range(len(stack)):
        if stack[i] == 1:               # 루트가 어디 있는지
            a = i + 1
        if stack[i] == int(N/2):        # N/2가 어디 있는지
            b = i + 1
    print(f'#{test_case}', a, b)