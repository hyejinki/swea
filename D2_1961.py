n = int(input())    # 테케 개수
for i in range(n):
    size = int(input()) 
    for r in range(size):    #정사각행렬 크기
        arr = [list(map(int, input().split())) for _ in range(size)] #2차원배열 입력
        rotated_90_arr = [[0]*size for _ in range(size)]
        rotated_180_arr = [[0]*size for _ in range(size)]
        rotated_270_arr = [[0]*size for _ in range(size)]
        for j in range(size):   # 1행부터 3행까지
            for k in range(size):   
                rotated_90_arr[j][k] = arr[size-1-k][j]    # 90도 / 인덱스는 size-1 
                rotated_180_arr[j][k] = arr[size-1-j][size-1-k]
                rotated_180_arr[j][k] = arr[k][size-1-j]   
            print(''.join(map(str, rotated_90_arr[j], rotated_180_arr[j], rotated_270_arr[j])))
            
    

2