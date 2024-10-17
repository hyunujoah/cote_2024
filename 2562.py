import sys
numbers=[] #리스트 초기화
for _ in range(9):
    number=int(sys.stdin.readline().strip())
    numbers.append(number)

print(max(numbers))
print(numbers.index(max(numbers))+1)