def nCr(C, L, s):
    global new_comb
    if L == 0:
        cnt = 0         # 자음 2개 이상
        flag = 0        # 모음 하나 이상이면 ==1
        for x in comb:
            if x in v:
                flag = 1
            else:
                cnt += 1
        if flag == 1 and cnt >= 2:
            new_comb.append(sorted(comb))   # 통과한 애들은 new에 넣어줌

    else:
        for i in range(s, C-L+1):
            comb[L-1] = A[i]
            nCr(C, L-1, i+1)
L, C = map(int, input().split())
A = list(input().split())
v = ['a', 'e', 'i', 'o', 'u']               # 모음
comb = [0]*L                                # 조합 들어갈 리스트
new_comb = []                               # 조건에 맞는 조합들 모아(global)
nCr(C, L, 0)

ans = sorted(new_comb)                      # 만든 조합 정렬할 거
for i in range(len(ans)):               # 출력이 ㄲㅏ다로웠음
    res = ''
    for x in ans[i]:
        res += x
    print(res)