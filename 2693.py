import sys
n=int(sys.stdin.readline().strip())

for i in range(n):
    numbers=list(map(int,sys.stdin.readline().strip().split()))
    numbers.sort() #sort함수는 배열 또는 리스트의 요소들을 정렬하는 함수
    print(numbers[-3]) #[-3]은 뒤에서 세 번째 요소를 뜻한다