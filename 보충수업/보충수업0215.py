# 계산기 1
def get_postfix(infix, n):
    postfix = ''
    stack = []

    # i번째 글자에 대해서 연산자면 스택에 넣고 피연산자면 결과에 출력
    for i in range(n):
        # 피연산자면 출력
        if '0' <= infix[i] <= '9':
            postfix += infix[i]
        # 연산자였다
        else:
            # 스택이 비어있지 않으면
            if stack:
                postfix += stack.pop()

            stack.append(infix[i])
    # 스택이 빌때까지 남은 연산자를 결과에 출력
    while stack:
        postfix += stack.pop()

    return postfix

def get_result(postfix):
    stack = []

    # 후위 표기식에서 글자를 하나씩 가져와서 계산
    for c in postfix:
        # 피연산자인 경우 스택에 넣기
        if '0' <= c <= '9':
            stack.append(int(c))
        # 연산자인 경우 계산
        else:
            right = stack.pop()
            left = stack.pop()

            result = right + left
            # 다음 연산을 위해 현재 결과를 스택에 저장
            stack.append(result)
    return ??

for tc in range(1, 11):
    n = int(input())
    exp = input()

    # 1. 후위표기식으로 변환
    postfix = get_postfix(exp, n)

    # 2. 후위표기식을 계산
    answer = get_postfix(postfix)

    print(answer)