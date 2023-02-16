def f(i, k):
    global minV
    if i == k:          # 순열 완성
        s = 0

        for j in range(N):
            s += arr[j][p[j]]   # j행에서 고른 열 p[j]
        if minV > s:
            minV = s
        return
    else:
        for j in range(i, N):   # p[i]의 숫자를 자신부터 오른쪽과 교환해볼게
            p[i], p[j] = p[j], p[i]
            f(i+1, k)
            p[i], p[j] = p[j], p[i]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    p  = [i for i in range(N)]      # p[i] i행에서 선택한 열
    minV = 30                        # 자연수
    print(f(0, N))