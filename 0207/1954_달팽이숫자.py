# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]          # 오 아래 왼 위
# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
#     dir = 0             # 진행방향
#     i = j = 0           # 숫자를 쓸 칸의 인덱스
#     for k in range(1, N*N+1):
#         arr[i][j] = k
#         ni, nj = i + di[dir], j + dj[dir]       # 다음 숫자를 쓸 좌표
#         if 0 <= ni < N and 0 <=nj < N and arr[ni][nj] == 0: 
#             i, j = ni, nj
#         else:                       # 배열을 벗어나거나 이미 숫자가 있으면
#             dir = (dir + 1) % 4     # 다음 방향으로 전환
#             i, j = i + di[dir], j + dj[dir]
#     print(f'#{test_case}')
#     for x in arr:
#         print(*x)

# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
 
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0]*N for _ in range(N)]
 
#     dir = 0     # 진행방향
#     i = j = 0   # 숫자를 쓸 칸의 인덱스
#     for k in range(1, N*N+1):
#         arr[i][j] = k
#         ni, nj = i+di[dir], j+dj[dir]   # 다음 숫자를 쓸 좌표
#         if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0:    # 숫자를 쓸 수 있으면
#             i, j = ni, nj
#         else:               # 배열을 벗어나거나 이미 숫자가 있으면
#             dir = (dir + 1) % 4 # 다음 방향으로 전환
#             i, j = i + di[dir], j + dj[dir]
 
#     print(f'#{tc}')
#     for x in arr:
#         print(*x)


# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]
# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     arr = [[0] * N for _ in range(N)]

#     i = j = dr = 0  # 초기값 설정
#     for cnt in range(1, N * N + 1):
#         arr[i][j] = cnt  # 현재좌표에 숫자 기록
#         ni, nj = i + di[dr], j + dj[dr]  # 이동할 위치 계산

#         # 이동할 위치가 범위내 and 빈칸(==0)인경우 이동
#         if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
#             i, j = ni, nj
#         else:  # 방향을 꺽어서 이동위치 다시 계산
#             dr = (dr + 1) % 4  # 0-1-2-3-1-2..
#             i, j = i + di[dr], j + dj[dr]

#     print(f'#{test_case}')
#     for lst in arr:
#         print(*lst)


dij = [[-1, 0], [0, 1], [1, 0], [0, -1]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    i = j = dir = 0     # 초기값
    for k in range(1, N*N+1):
        arr[i][j] = k           # 현재 좌표에 숫자 기록
        ni, nj = i + dij[dir][0], j + dij[dir][1] # 이동할 위치 계산
        # 이동할 위치가 범위내, 빈칸인 경우 이동
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i, j = ni, nj
        else:       # 방향을 꺾어서 이동 위치 다시 계산
            dir = (dir + 1) % 4   # 0-1-2-3-1-2
            i , j = i + dij[dir][0], j + dij[dir][1]

    print(f'#{tc}')
    for s in arr:
        print(*s)
  
