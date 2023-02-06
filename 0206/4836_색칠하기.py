# T = int(input())
# for test_case in range(1, T+1):
#     N = int(input())
    # red_coor = []
    # blue_coor = []
    # total = []
    # for i in range(N):
    #     l = list(map(int, input().split()))
    #     start = [l[0], l[1]]
    #     end = [l[2], l[3]]
    #     color = l[4]
    #     for x in range(start[0], end[0] + 1):
    #         for y in range(start[1], end[1] + 1):
    #             coor = (x, y)
    #             if color == 1:          # red끼리 좌표 다 더해
    #                 red_coor.append(coor)
    #             if color == 2:          # blue끼리 좌표 다 더해
    #                 blue_coor.append(coor)
    # total = red_coor + blue_coor
    #
    # print(f'#{test_case}', len(total) - len(set(total)))

# 줄이기
T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    total = []
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for p in range(r1, r2+1):
            for q in range(c1, c2+1):
                pq = (p, q)
                total.append(pq)
    print(f'#{test_case}', len(total) - len(set(total)))
