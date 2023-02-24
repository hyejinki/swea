T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    ans = 0
    for x in range(1, int(N**(1/3))+2):
        if x**3 == N:
            break
        else:
            x = -1
    print(f'#{test_case}', x)
