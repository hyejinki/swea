# 특정 수의 배수 찾기

# 10 미만의 자연수에서 2와 7의 배수를 구하면 2,4,6,7,8이다. 이들의 총합은 27이다
# 1000미만의 자연수에서 2,7의 배수의 총합을 구하라.

list_multi = []
for i in range(20):
    # 2의 배수
    if i % 2 == 0:
        list_multi.append(i)
    # 7의 배수
    elif i % 7 == 0:
        list_multi.append(i)
# set으로 중복 제거     
print(sum(set(list_multi)))
