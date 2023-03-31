
def f(n, string, ci, cj):
    if n == 7:
        sset.add(string)
        return
    for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            f(n + 1, string+str(arr[ni][nj]), ni, nj)

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split()))for _ in range(4)]
    sset = set()
    for i in range(4):
        for j in range(4):
            f(0, '', i, j)

    print(f'#{test_case}', len(sset))