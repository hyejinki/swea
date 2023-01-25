# 카페 메뉴 주문 받기 예제
# 1. 아이스 음료 주문이 몇 개 들어왔는지 확인하세요
# 2. 메뉴 별 주문 수를 출력하세요

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
lis_order = orders.split(',')

# 아이스로 시작하면 리스트에 넣어준다
ice_lis = [word for word in lis_order if '아이스' in word]
print(len(ice_lis))

# 메뉴 별 주문 수 딕셔너리로 출력
count = {}
for i in lis_order:
    try : count[i] += 1
    except : count[i] = 1
print(count)