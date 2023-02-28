T = int(input())
for test_case in range(1, T+1):
    memory = [0] + list(map(int, input()))      # 0에서 1로 바뀌는 걸로 시작해야하니까
    count = 0
    for i in range(len(memory)-1):
        if memory[i] != memory[i+1]:        # 뒤가 다르면 카운트
            count += 1
    print(f'#{test_case}', count)
        