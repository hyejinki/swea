T = int(input())
for test_case in range(1, T+1):
    str1 = input()
    ans = 0
    for i in range(int(len(str1)/2)):
        if str1[i] != str1[len(str1)-i-1]:
            break
        else:
            ans = 1
    print(f'#{test_case}', ans)