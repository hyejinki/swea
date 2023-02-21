T = int(input())
for test_case in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0]*1020
    front = rear = -1
    for x in arr:           # arr요소 push
        rear += 1
        queue[rear] = x
    for i in range(M):
        front += 1                  # pop
        rear += 1                   # push
        queue[rear] = queue[front]

    print(f'#{test_case}', queue[front+1])