import sys
test_case=int(sys.stdin.readline().strip())
#[2:]는 인덱스 2부터 끝까지의 요소를 출력
#[:2]는 처음부터 인덱스 2 직전까지의 요소를 출력
for _ in range(test_case):
    n=int(sys.stdin.readline().strip())
    binary_number=bin(n)[2:] #이진수로 변환, bin만하면 0b1101이 출력이되는데 [2:]로 0b는 출력하지 않는다
    #bin()함수는 정수를 이진수 문자열로 반환한다
    for i in range(len(binary_number)):
        if binary_number[-i-1]=='1':
            print(i,end=' ') #인덱스 값 출력