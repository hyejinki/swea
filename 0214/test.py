N = int()
top = -1
stack = [0] * N
for tc in range(N):
    command = list(map(str, input().split()))
    if command[0] == 'push':
        top += 1
        stack[top] = int(command[1])
    elif command[0] == 'pop':
        if top > -1:
            print(stack[top])
            top -= 1
        else:
            print(-1)
    elif command[0] == 'size':
        print(top+1)
    elif command[0] == 'empty':
        if top > -1:
            print(0)
        else:
            print(1)
    elif command[0] == 'top':
        if top > -1:
            print(stack[top])
        else:
            print(-1)