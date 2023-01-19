# 1959_두 개의 숫자열

T = int(input()) 
for test_case in range(1, T + 1):
    N, M = map(int, input().split())      
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))
    res = []
    for j in range(M-N+1):
        sum = 0
        for i in range(N):  
            mul_ans = A_arr[i]*B_arr[i+j] 
            print (A_arr[i])
            print (B_arr[i+j])
            sum += mul_ans
    res.append(sum)
   
    print (f"#{test_case} {max(res)}")