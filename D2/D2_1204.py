# 1204_최빈수 구하기
n = int(input())    #테스트 케이스 개수
for i in range(n):
    order = int(input()) # 순서번호
    input_value = list(map(int,input().split())) #숫자들 입력
    max_value = 1 + max(input_value) # 리스트에서 가장 큰 값
    list_value = [0]*(max_value) #가장 큰 값 만큼의 개수를 가진 리스트 생성
    for j in input_value:
        list_value[j] += 1 #해당 인덱스에 개수만큼 카운트

    for k in range(max_value):
        if list_value[k] == max(list_value):
            num = k
    print (f"#{order} {num}")

