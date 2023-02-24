def inorder_t(i, N):           # 중위순회
    if i <= N:
        inorder_t(2*i, N)       # 왼
        stack.append(i)
        inorder_t(2*i+1, N)     # 오
    else:
        return

for test_case in range(1, 11):
    N = int(input())
    dic = {}
    for i in range(N):
        info = list(map(str, input().split()))
        dic[i+1] = info[1]

    stack = []              # 탐색 순서대로
    inorder_t(1, N)
    ans = ''
    for x in stack:         # 딕셔너리 value출력
        ans += dic[x]

    print(f'#{test_case}', ans)