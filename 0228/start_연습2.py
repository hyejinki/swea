# 16진수 -> 2진수
arr = input()
for x in arr:
    num = int(x, 16)
    for j in range(3, -1, -1):
        bit = 1 if num&(1<<j) else 0
        print(bit, end='')
        # print(bit)
    print(' ', end = '')    # 빈 칸


