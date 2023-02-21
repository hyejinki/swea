import sys
from collections import deque

T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().strip().split())
    imp = deque(list(map(int, sys.stdin.readline().strip().split())))
    dic = {}
    for i in range(N):  # key : 인덱스  value : 중요도
        dic[i] = imp[i]
    i = 0
    count = 0
    while True:
        maxV = 0
        for x in imp:
            if x > maxV:
                maxV = x
        if maxV == imp[0]:  # 맨 앞에 가장 중요한 문서라면 pop
            count += 1
            imp.popleft()
            if maxV == dic[M]:
                break
        else:
            imp.append(imp.popleft())  # 맨 뒤로 보내


    print(count)