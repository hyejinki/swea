def comb(li, n):
    result = []
    if n > len(li):
        return result

    if n == 1:
        for i in li:
            result.append([i])
    else:
        for i in range(len(li) - n + 1):
            for j in comb(li[i+1:], n-1):
                result.append([li[i]] + j)

    return result

N, M = map(int, input().split())

num_li = []

for i in range(1, N+1):
    num_li.append(i)
# 조합 출력
ans = comb(num_li, M)
for v in ans:
    print(*v)