 # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 4.0% 700.0g
# 변수 선언
li_salt = []
all_brine = 0
# 반복문
while True:
    for i in range(1,6):
        ans = input(f'{i}. 소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: ')
        if ans != 'Done':   
            density, brine = list(map(lambda n: int(n[:-1]), ans.split()))  # 농도와 소금물의 양
            salt = (density * brine) / 100   # 소금의 양
            li_salt.append(salt)             # 소금의 양을 리스트에 넣어줌
            all_brine += brine
        else :
            break
    res = (sum(li_salt) * 100) / all_brine 
    if res:
        break
print(f'{res}% {all_brine}g')
            
