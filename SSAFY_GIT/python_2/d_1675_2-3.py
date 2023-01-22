# 문자열 슬라이싱에 대한 이해 예제

# 하나의 문장을 입력받아, 그 문장에 끝말잇기 규칙을 적용시켜보려 한다.
# 세 단어가 입력으로 주어졌을 때 그 끝말잇기가 옳으면 Pass, 옳지 않으면 Fail을 출력하시오
# 예를 들어 saFe eMotion Nail인 경우, pass를 출력한다.
word_list = []
str_lst = input('문자열을 입력하세요. : ')
# 문자열을 다 대문자로 바꾼다
str_lst = str_lst.upper()
word_list = str_lst.split(' ')

# 두번 확인 
for i in range(2):
    # 첫 단어의 마지막 인덱스와 그 다음 단어의 첫 번째 인덱스 확인
    if word_list[i][-1] != word_list[i+1][0]:
        print('False')
        break
else:
    print('Pass')
        
