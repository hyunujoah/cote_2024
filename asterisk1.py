import sys
n=int(sys.stdin.readline().strip()) #입력이 5라고 가정
for i in range(n): #0~4까지 반복
    for _ in range(i+1): #0~4까지 반복
        print('*',end='') #end=''는 줄 바꿈 문자 대신 아무것도 추가하지 않고 출력을 종료하겠다는 것을 의미한다
    if i != n-1:
        print()


#for i in range(n+1):
#    print('*'*i)