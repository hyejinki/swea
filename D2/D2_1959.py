# 1959_두 개의 숫자열

T = int(input()) 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))
    ans = 0
    for j in range(M-N+1):
        for i in range(N):
            mul_ans = A_arr[i]*B_arr[j]
           


    
    print (f"#{test_case} {ans}")