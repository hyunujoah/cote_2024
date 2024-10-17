import sys
#입력은 총 28줄 n(1부터 30까지)
students=[i for i in range(1,31)] #리스트 컴프리헨션 초기화
#Tip:i for i in range(1,31) 형태는 반드시 특정 구문으로 감싸야 한다!
#리스트 컴프리헨션 양식, [표현식 for 요소 in iterable]

for _ in range(28):
    number=int(sys.stdin.readline().strip())
    students.remove(number)

print(min(students))
print(max(students))