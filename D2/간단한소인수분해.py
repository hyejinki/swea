

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    li = [2,3,5,7,11]
    new_li = [0]*5
    while(N != 1):
        for i in range(len(li)):
            if N % li[i] == 0:
                N = N / li[i]
                new_li[i] += 1
                break
    print(f'#{test_case}', *new_li)