T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    c = list(map(int, input().split()))
    t = list(map(int, input().split()))
    c.sort()
    t.sort(reverse=True)
    sum = 0
    for x in t:
        i = len(c) - 1
        while c:
            if x >= c[i]:
                sum += c[i]
                c.pop()
                break
            else:
                i -= 1
                c.pop()
    print(f'#{test_case}', sum)