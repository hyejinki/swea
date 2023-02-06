T = int(input())
for test_case in range(1, T+1):
    distance, A, B, fly = map(int, input().split())
    time = distance / (A + B)
    print(f'#{test_case}', time*fly)