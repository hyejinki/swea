# 백만이하 양수 중 소수
N = 1000000
pnumber = [1]*(N+1)
for i in range(2, N+1):
    if pnumber[i]:
        j = 2
        while i*j <= N:
            pnumber[i*j] = 0
            j += 1

for i in range(2, N+1):
    if pnumber[i]:
        print(i, end = ' ')