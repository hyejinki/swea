# # bubble
# arr = [55, 7, 78, 12, 42]
# N = len(arr)
# for i in range(N-1,0,-1):
#     for j in range(i):
#         if arr[j] > arr[j+1]:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)

# # 카운팅 정렬
# arr = [0, 4, 1, 3, 1, 2, 4, 1]
# arr_sort = [0]*len(arr)
# maxV = 0
# for i in range(len(arr)):
#     if maxV < arr[i]:
#         maxV = arr[i]
# counts = [0] * (maxV+1)

# for i in range(len(arr)):
#     counts[arr[i]] += 1

# for i in range(1, len(counts)):
#     counts[i]  += counts[i-1]

# for i in range(len(arr_sort)-1, -1, -1):
#     counts[arr[i]] -= 1
#     arr_sort[counts[arr[i]]] = arr[i]

# print(arr_sort)


# # 소수 찾기
# N = 100000
# pnumber = [1]*(N+1)
# for i in range(2, N+1):
#     if pnumber[i]:
#         j = 2
#         while i*j <= N:
#             pnumber[i*j] = 0
#             j += 1

# for i in range(2, N+1):
#     if pnumber[i]:
#         print(i, end = ' ')


# #풍선팡
# T = int(input())
# for test_case in range(1, T+1):
#     N, M = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     di = [0, 1, 0, -1]
#     dj = [1, 0, -1, 0]
#     maxV = 0
#     for i in range(N):
#         for j in range(M):
#             temp_sum = 0
#             for k in range(4):
#                 for l in range(1, arr[i][j]+1):
#                     ni, nj = i+di[k]*l, j+dj[k]*l
#                     if 0 <= ni < N and 0 <= nj < M:
#                         temp_sum += arr[ni][nj]
#             if temp_sum + arr[i][j] > maxV:
#                 maxV = temp_sum + arr[i][j]
#     print(maxV)


# 

