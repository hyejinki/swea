# def promising(i, j):
#     if col[j] or d1[i + j] or d2[i + N - 1 - j]:
#         return 0
#     return 1


def f(i, N):
    global cnt
    if i == N:                  # N개의 퀸을 놓은 경우
        cnt += 1
    else:
        for j in range(N):
            # if promising(i, j):
            if col[j] == 0 and d1[i + j] ==0 and d2[i + N - 1 - j] == 0:
                col[j] = 1
                d1[i + j] = 1
                d2[i + N - 1 - j] = 1
                f(i+1, N)
                col[j] = 0
                d1[i + j] = 0
                d2[i + N - 1 - j] = 0



T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    col = [0] * N
    d1 = [0] * (N + N - 1)          # / 방향 대각선
    d2 = [0] * (N + N - 1)          # \ 방향 대각선
    cnt = 0
    f(0, N)
    print(f'#{tc}', cnt)