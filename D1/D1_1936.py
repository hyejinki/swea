a, b = map(int, input().split()) 
if a-b > 0: # A가 이기는 경우
    print('A')
elif a-b < 0:   # B가 이기는 경우
    print('B')