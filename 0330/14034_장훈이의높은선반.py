def f(l, r, B, s):
    global minV
    if s == B:
        return s
    elif s > B:
        if minV > B - s:
            minV = s - B
    else:
        if l > r:
            return -1
    
        f(l+1, r, B, s + arr[l]) # 더하거나
        f(l+1,r, B, s)
        
                     # 통과하거나  

T = int(input())
for test_case in range(1, T + 1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    a = 0
    minV = 10000
    f(0, N - 1, B, 0)
    print(f'#{test_case}', minV)
