T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    str2 = ''           # 새로 문자를 받을 str2
    for i in str1:
        if i == 'b':
            str2 += 'd'
        elif i == 'd':
            str2 += 'b'
        elif i == 'p':
            str2 += 'q'
        elif i == 'q':
            str2 += 'p'
    print(f'#{test_case}', str2[::-1])      # 거꾸로
