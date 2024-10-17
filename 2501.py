import sys
n,k=map(int,sys.stdin.readline().strip().split())
#map함수란? 여러 개의 데이터를 한 번에 다른 형태로 변환할 때 사용한다

list=[] #빈 리스트를 생성

for i in range(1,n+1): #n, 입력 숫자
    if n%i==0:
        list.append(i)

if len(list)<k:
    print(0)
else:
    print(list[k-1]) #인덱스 번호에 맞춰야 하기 때문에 k-1