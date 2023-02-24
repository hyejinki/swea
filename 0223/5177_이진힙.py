def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[c] < heap[p]:      # 부모가 있고 자식보다 더 크면
        heap[c], heap[p] = heap[p], heap[c] # 바꿔
        c = p                               # 변환 후 확인
        p = c // 2

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    heap = [0] * (N+1)
    last = 0
    for x in arr:
        enq(x)
    ans = 0
    while(N > 0):
        ans += heap[N//2]       # 조상들의 합
        N = N//2
    print(f'#{test_case}', ans)