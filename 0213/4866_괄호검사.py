T = int(input())
for test_case in range(1, T+1):
    s = input()
    stack = [0] * len(s)
    top = -1
    ans = 1
    for x in s:
        if x == '(' or x == '{':
            top += 1
            stack[top] = x                  # (, { push
        elif x == ')':
            if top > -1:
                if stack[top] == '(':       # 이전에 올바른 짝이 있다면 인덱스만 내려줌
                    top -= 1
                else:
                    ans = 0
            else:
                ans = 0
        elif x == '}':                      # 동일
            if top > -1:
                if stack[top] == '{':
                    top -= 1
                else:
                    ans = 0
            else:
                ans = 0
    else:                                   # 여는 괄호가 남아있으면 오류
        if top > -1:
            ans = 0
    print(f'#{test_case}', ans)