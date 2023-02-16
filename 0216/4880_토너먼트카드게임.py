def r_s_p_game(a, b):
    global s
    i = s[a]        # i: a의 카드
    j = s[b]        # j: b의 카드
    if (j == 1 and i == 3) or (j == 2 and i == 1) or (j == 3 and i == 2):
        return b            # b가 이긴 경우
    else:                   # 비기거나 a가 이긴 경우
        return a

def f(arr, a, b):   # a, b -> 시작점, 개수
    if a == b:
        return a
    mid = (a + b) // 2
    r1 = f(arr, a, mid)
    r2 = f(arr, mid+1, b)
    return r_s_p_game(r1, r2)

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    s = list(map(int, input().split()))
    print(f'#{test_case}', f(s, 0, N-1)+1)

