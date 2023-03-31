def Btrans(li, n):
    x = 0
    for i in range(n):
        x += li[n - 1- i] * (2**i)
    return x

def Ttrans(li, n):
    x = 0
    for i in range(n):
        x += li[n - 1 - i] * (3**i)
    return x

T = int(input())
for test_case in range(1, T + 1):
    bi = list(map(int,input()))
    tr = list(map(int,input()))
    i = 0
    flag = 1
    while i < len(bi):
        tmp = bi[:]
        if bi[i] == 0:
            tmp[i] = 1
        else:
            tmp[i] = 0
        ans = Btrans(tmp, len(bi))

        for j in range(len(tr)):
            tmp2 = tr[:]
            for k in [0, 1, 2]:
                tmp2[j] = k

                if Ttrans(tmp2, len(tr)) == ans:
                    flag = 0
                    break
            if flag == 0:
                break
        if flag == 0:
            print(f'#{test_case}', ans)
            break
        i += 1

