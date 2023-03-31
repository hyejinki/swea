def f(i):  # i 는 리스트 길이
    for t in range(2, i // 2 + 1):
        # if ans[i][i - t - k - 1] == ans[i][i - k - 1]:
        if i - (2 * t) - 1 < 0:
            a = ans[i][i - 1 - t::-1]
        else:
            a = ans[i][i - 1 - t:i - (2 * t) - 1:-1]
        if ans[i][i - 1:i - t - 1:-1] == a:
            return 0
    return 1

N = (int(input()))
ans = ['0'] * 81
num = [1, 2, 3]
ans[1] = '1'

if N > 3:
    x = 2
    i = 0
    while x <= N:
        for i in num:
            if num[i] != int(ans[x - 1][-1]):
                ans[x] = ans[x - 1] + str(num[i])
                if f(x) == 1:
                    x += 1
                    i = 0
                else:
                    i += 1

            else:
                i += 1
            if i > 2:
                pass


print(int(ans[N]))