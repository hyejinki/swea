# 1974_스도쿠 검증
def transpose(arr): #열 체크를 위한 전치행렬 구하기
    row = 9
    col = 9
    arr_T = [[0]*9 for _ in range(9)]

    for i in range(row):
        for j in range(col):
            arr_T[j][i] = arr[i][j]
    return (arr_T)

def check():
    #행 체크
    for i in range(size):
        if len(set(arr[i])) != 9:  #중복 제거하고 크기를 확인했을 때 9가 나와야 모든 숫자가 있는 것
            return 0
    #열 체크
    arr_T = transpose(arr)
    for i in range(size):
        if len(set(arr_T[i])) != 9:
            return 0
    #박스 체크       
    for i in range(0, 9, 3):    #0부터 9까지 3씩 증가 -> 0 3 7
        for j in range(0, 9, 3):
            box = arr[i][j:j+3] + arr[i+1][j:j+3] + arr[i+2][j:j+3]
            if len(set(box)) != 9:
                return 0
    return 1


T = int(input()) 
for test_case in range(1, T + 1):
    size = 9
    arr = [list(map(int, input().split())) for _ in range(size)]

    ans = check()

    print (f"#{test_case} {ans}")
    
