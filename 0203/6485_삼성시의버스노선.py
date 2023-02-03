T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    route = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    C = [(int(input()) for _ in range(P))]
    ans_arr = [0]*P                 # 답을 담은 배열
    for i in range(N):              # N 개의 버스 노선
        for j in range(P):     # 확인할 P개의 정류장
            if route[i][0] <= C[j] and C[j] <= route[i][1]:     # C의 원소가 노선에 해당한다면
                ans_arr[j] += 1

    print(f'#{test_case}', *ans_arr)