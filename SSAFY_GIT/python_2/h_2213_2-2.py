# 카페 주문 건수 출력하기 예제
# 다음은 한 커피전문점의 주문 대기목록입니다. 주어진 문자열을 가지고, 프로그램을 작성하세요
# 1. 총 몇 잔의 주문이 들어왔는지 확인하세요.
# 2. 중복을 제거한 메뉴만을 리스트 형식으로 출력하세요(내림차순)

orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'
# ','를 기준으로 분리해서 리스트에 넣는다.
list_order = orders.split(',')
# 총 몇 잔인지 확인
print(f'{len(list_order)}잔 주문 들어왔습니다.')

# 중복 제거하고 주문 수대로 내림차순으로 정렬
# 리스트 중복 요소 개수 찾기 -> 딕셔너리로 표
count = {}
for i in list_order:
    try: count[i] += 1
    except: count[i] = 1
# 딕셔너리 정렬 (key값 출력)
ans = sorted(count.keys(), reverse=True)
print(ans)