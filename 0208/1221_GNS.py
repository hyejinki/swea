T = int(input())
for tc in range(1, T+1):
    N = input()
    arr = list(map(str, input().split()))
    dic = {}
    ans = ''
    for i in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]:
    for i in ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]:
        for j in range(dic[i]):         # value 만큼 i 출력
            ans += i +' '
    print(f'#{tc}\n ', ans)