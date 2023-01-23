# 딕셔너리와 리스트 특징 이해

# tuple로 저장한 list가 있다. 각 첫 번째 요소는 해야할 일, 두 번째 요소는 남은 일 수이다.
# 새로운 일정을 입력받아 list에 추가하고 출력하라

todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]
#입력 받은 '해야할 일'과 '남은 일 수'를 튜플로 묶는다
work = str(input())
day = int(input())
new_tup = (work, day)
todo.append(new_tup)

print(todo)
