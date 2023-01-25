# for문을 활용하여 리스트 변환 예제
# 문자열 안의 rottend 다 없애기

string = input()
# 문자열 다 소문자로 바꿔주고 시작
string = string.lower()
# ',' 을 기준으로 구분해서 리스트에 넣어준다.
rot_list = string.split(',')
ans_lis = []
# 리스트 안에 rotten이 있는 단어를 찾고 'rotten'을 ''로 바꿔준다
for word in rot_list:
    if 'rotten' in word:
        new_word = word.replace('rotten','')
        ans_lis.append(new_word)
    else:
        ans_lis.append(word)
print(ans_lis)