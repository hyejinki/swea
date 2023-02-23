# 우선순위 큐
# 최대 100개의 key
# 최대 힙 구현 - 루트에 가까워질수록 값이 커지게 만들기

def enq(n): # 인큐
    global last
    last += 1
    heap[last] = n
    c = last # 부모 > 자식 확인을 위해
    p = c//2
    while p > 0 and heap[p] < heap[c]: # 부모가 있는데 자식보다 작은 값을 가졌다면
        heap[p], heap[c] = heap[c], heap[p] # 자리바꿔
        c = p # 옮긴 자리에서 부모와 비교하기 위해
        p = c//2
    return

heap = [0] * 101 # 완전이진트리. 1번 ~ 100번 인덱스 준비
last = 0 # 마지막 정점 번호
enq(5)
print(heap[1]) # 루트 노드의 키 값 꺼내기 # 5
enq(15)
print(heap[1]) # 15
enq(8)
print(heap[1]) # 15
enq(20)
print(heap[1]) # 20


def deq(): # 디큐
    global last
    tmp = heap[1] # 루트 노드의 키 값 임시 저장
    heap[1] = heap[last] # 마지막 정점의 값을 루트로 이동
    last -= 1 # 마지막 정점 삭제
    p = 1
    c = p*2 # 왼쪽 자식 번호
    while c <= last: # 자식이 하나 이상 있으면
        if c+1 <= last and heap[c] < heap[c+1]: # 오른쪽 자식 있고 오른쪽 자식의 키 값이 더 크면
            c += 1 # 비교대상을 오른쪽 자식으로 변경
        if heap[c] > heap[p]: # 자식이 부모보다 크면
            heap[c], heap[p] = heap[p], heap[c] # 자리바꿔
            p = c
            c = p*2
        else:
            break
    return tmp

while last > 0:
    print(deq())
'''
20
15
8
5
'''