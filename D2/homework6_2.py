# # A.    입력 예시 
# # ['nat,'eat','tea','tan','ate','bat']

# # B.    출력 예시 
# # [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 


dict = {}
li = list(map(str,input().split(',')))
for i in li:
    word= ''.join(sorted(i))
    dict[word] = dict.get(word,[]) + [i]
print(dict.values())