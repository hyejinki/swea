T = int(input())
for test_case in range(1, T+1):
    s = list(input().split())
    stack = [0] * len(s)
    top = -1
    op = {'+', '*', '-', '/'}
    for x in s:
        if '0' <= x[0] <= '9':           # 숫자라면 push
            top += 1
            stack[top] = int(x)
        if x == '.':
            break
        elif x in op:                   # 연산자면
            if top > 0:                 # 앞에 숫자가 두 개 이상 있으면
                top -= 1                # pop
                if x == '+':
                    stack[top] = stack[top] + stack[top + 1]
                elif x == '-':
                    stack[top] = stack[top] - stack[top + 1]
                elif x == '*':
                    stack[top] = stack[top] * stack[top + 1]
                else:
                    stack[top] = int(stack[top] / stack[top + 1])
            else:
                ans = 'error'
                break
        ans = stack[top]

    if stack == [0] or top > 0:                # 빈 스택이면 error
        ans = 'error'

    print(f'#{test_case}', ans)

