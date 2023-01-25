# 게시판의 페이지 수 구하기

import math

page = int(input('게시글의 총 갯수를 입력하세요 : '))
w = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))
ans = math.ceil(page / w)

print(ans)



# 모듈 안 쓰고

# page = int(input('게시글의 총 갯수를 입력하세요 : '))
# w = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

# if page % w == 0:
#     print(int(page / w))
# else :
#     print(page // w + 1)