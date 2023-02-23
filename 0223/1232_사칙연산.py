def cal(r1, r2, x):         # 계산혀
    if x == '+':
        return r1 + r2
    elif x == '-':
        return r1 - r2
    elif x == '*':
        return r1 * r2
    else:
        return r1 // r2

def check(num):
    x = tree[num]
    op = ['+', '-', '*', '/']

    if tree[num] in op:
        r1 = check(left[num])          # 왼쪽 서브트리의 연산 결과
        r2 = check(right[num])         # 오른쪽 서브트리의 연산 결과
        return cal(r1, r2, x)
    else:
        return tree[num]

for test_case in range(1, 11):
    N = int(input())
    tree = [0] * (N + 1)
    left = [0] * (N + 1)            # 왼쪽 자식 번호
    right = [0] * (N + 1)           # 오른쪽 자식 번호
    for _ in range(N):
        arr = input().split()
        node = int(arr[0])
        if len(arr) > 2:        # 연산자인 경우
            tree[node] = arr[1]
            left[node] = int(arr[2])
            right[node] = int(arr[3])
        else:                   # 피연산자인 경우
            tree[node] = int(arr[1])

    print(f'#{test_case}', check(1))