for test_case in range(1, 11):
    N = int(input())
    s = list(input())
    stack = []
    temp = []

    for x in s:
        if '0' <= x <= '9':
            temp.append(int(x))
        else:
            if len(stack) < 1:
                stack.append(x)               # push
            else:
                stack.pop()                   # pop
                stack.append(x)
                temp.append(temp.pop() + temp.pop())       # temp에 있던 요소 pop과 합 동시에. 신기

    while stack:                # 스택이 빌 때까지
        stack.pop()
        temp.append(temp.pop() + temp.pop())

    print(f'#{test_case}', *temp)