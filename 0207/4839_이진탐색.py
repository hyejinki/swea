# 이진탐색 함수
def binary(total_page, n):
    l = 1                       # start
    r = total_page              # end
    i = 0                       # 카운트
    while l <= r:
        c = int((l+r)/2)
        if n == c:              # 값 찾으면 i반환

            return i
        elif n > c:
            l = c
        else:
            r = c
        i += 1

T = int(input())
for test_case in range(1, T+1):
    total_page, A, B = map(int, input().split())
    if binary(total_page, A) == binary(total_page, B):  # 비긴 경우
        ans = 0
    elif binary(total_page, A) > binary(total_page, B): # A가 더 오래 걸렸으니 B 승
        ans = 'B'
    else:
        ans = 'A'
    print(f'#{test_case}', ans)


