import sys
test_numbers=int(sys.stdin.readline().strip()) #테스트 숫자 갯수
numbers=list(map(int,sys.stdin.readline().strip().split())) #리스트 구현

#최솟값과 최댓값을 인덱스로 가져온다
min=numbers[0]
max=numbers[0]

#반복문을 이용하여 검사한다
for d in numbers[1:]: #인덱스 몇부터, 1부터 기준을 잡는다 min과 max를 인덱스 0으로 초기화하였기 때문에
    if d<min:
        min=d
    elif d>max:
        max=d

print(min,max)