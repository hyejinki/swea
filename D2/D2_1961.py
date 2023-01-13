def rotate(arr):
    rotated_arr = [[0]*size for _ in range(size)] # 행렬 크기만큼 생성
    for i in range(size):
        for j in range(size):
            rotated_arr[i][j] = arr[size-1-j][i] #90도 회전
    return rotated_arr


n = int(input()) #테케 개수
for N in range(n):
    size = int(input())
    num = [list(map(int, input().split())) for _ in range(size)] #2차원배열 입력
    rotated_90 = rotate(num)
    rotated_180 = rotate(rotated_90)
    rotated_270 = rotate(rotated_180)
    print(f"#{N+1}")
    for i in range(size):
        #for j in range(0,size):
        #print(''.join(rotated_90[i]), ''.join(rotated_180[i]), ''.join(rotated_270[i]))
        #print(''.join(map(str, rotated_90[i]+ rotated_180[i]+ rotated_270[i])))
        #print(*rotated_90[i], sep = '')
        print(*rotated_90[i][j], *rotated_180[i][j], *rotated_270[i][j], sep = '')
        
'''

n = int(input())    # 테케 개수
for i in range(n):
    size = int(input()) #정사각행렬 크기
    arr = [list(map(int, input().split())) for _ in range(size)] #2차원배열 입력
    rotated_90_arr = [[0]*size for _ in range(size)]
    rotated_180_arr = [[0]*size for _ in range(size)]
    rotated_270_arr = [[0]*size for _ in range(size)]
    for j in range(size):   # 1행부터 3행까지
        for k in range(size):   
            rotated_90_arr[j][k] = arr[size-1-k][j]    # 90도 / 인덱스는 size-1 
            rotated_180_arr[j][k] = arr[size-1-j][size-1-k]
            rotated_270_arr[j][k] = arr[k][size-1-j]   
        print(''.join(map(str, rotated_90_arr[j]+ rotated_180_arr[j]+ rotated_270_arr[j])))
'''