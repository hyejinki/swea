def f(i, k):
    if i == k:  # 목표에 도달하면
        print(B)
        return
    else:
        B[i] = A[i]
        f(i+1, k)

A = [10, 20, 30]
B = [0] * 3
f(0, 3)