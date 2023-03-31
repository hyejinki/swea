def hoare(A, l, r):
    p = A[l]
    i = l
    j = r
    while i <= j:
        while i <= j and A[i] <= p:
            i += 1
        while i <= j and A[j] >= p:
            j -= 1
        if i < j:
            A[i], A[j] = A[j], A[i]
    A[j], A[l] = A[l], A[j]         # 피봇 값을 경계에 위치시킴
    return j                        # 피봇의 위치 리턴

def qsort(A, l, r):
    if l < r:
        s = hoare(A, l, r)
        qsort(A, l, s - 1)
        qsort(A, s + 1, r)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    qsort(arr, 0, N -1)

    print(f'#{test_case}', arr[N//2])