# 2050_알파벳을 숫자로 변환

alphabet = input()
for i in alphabet:
    num = ord(i)-64
    print(num,end=" ")