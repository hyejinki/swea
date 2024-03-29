'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def inorder(i):
    if i:           # 존재하는 정점이면
        inorder(left[i])
        print(i, end=' ')
        inorder(right[i])
    return


def postorder(i):
    if i:  # 존재하는 정점이면
        postorder(left[i])
        postorder(right[i])
        print(i, end=' ')
    return

def preorder(i):
    if i:           # 존재하는 정점이면
        print(i, end=' ')
        preorder(left[i])
        preorder(right[i])
    return

# 부모를 인덱스로 자식번호 저장
V = int(input())
arr = list(map(int, input().split()))
E = V - 1               # 간선수
left = [0] * (V + 1)    # 부모를 인덱스로 왼쪽 자식 저장
right = [0] * (V + 1)   #   "           오른쪽 자식 저장
par = [0] * (V + 1)     # 자식을 인덱스로 부모 저장
# child = [[]for _ in range(V+1)]
for i in range(E):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p
    # child[p].append(C)
root = 1
while par[root] != 0:       # root 찾기
    root += 1
preorder(root)
print()
inorder(root)
print()
postorder(root)
