# 문자열 메소드 이해 및 문제 해결

# HTML 문서의 text 양 옆에 태그가 있다. HTML text를 입력받아 P태그를 지우고 나머지 text 출력
# P 태그는 <p>와 </p>이다.

# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.

text = input()
for i in text:
    if i in '</p>':
        text = text.replace(i, '')

print(text)
