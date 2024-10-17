import sys #오리문제 어렵다..

crying=sys.stdin.readline().strip()
#quqacukqauackck 15
size=len(crying)
visited=[0]*size
count=0
quack="quack" #quack이라는 변수에 quack이라는 문자열을 저장한다

if size%5!=0:
    print(-1)
    exit() #프로그램 종료시킨다

def solution(start):
    global count #global 키워드를 사용하여 해당 변수가 전역 변수임을 명시적으로 지정
    index=0
    temp=True
    for i in range(start,size):
        if crying[i]==quack[index] and visited[i]==0: #두개 다 참이어야 실행
            visited[i]=1
            if quack[index]=='k':
                if temp: #temp가 True이면 실행
                    count+=1
                    temp=False
                index=0
            else:
                index+=1

for i in range(size):
    solution(i)

if count==0 or not all(visited):
    #all() 함수는 반복 가능한 객체를 인자로 받고, 그 객체의 모든 요소가 참이면 True를 반환한다
    #하나라도 0이면 all(visited)는 False가 되고 결과적으로 not all(visited)는 참이 된다
    print(-1)
else:
    print(count)