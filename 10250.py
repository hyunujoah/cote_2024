import sys
test_case=int(sys.stdin.readline().strip())
for _ in range(test_case): #test_case만큼의 반복을 수행한다
    h,w,n=map(int,sys.stdin.readline().strip().split())
    q,r=divmod(n-1,h) #divmod함수를 이용하여 몫과 나머지 값을 반환해준다
    print((r+1)*100+q+1) #연산 수식을 활용한다