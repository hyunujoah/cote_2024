import sys
def check():
    temp=0
    #가로
    for i in range(5):
        if bingo[i]==[0]*5:
            temp+=1
    #해당 코드는 row 부분을 확인한다

    #세로
    for i in range(5):
        if all(bingo[j][i]==0 for j in range(5)):
            #all은 iterable 내의 모든 요소가 참일 때 True 반환
            #아니면 False를 반환한다
            temp+=1
    #해당 코드는 column 부분을 확인한다


    #대각선1, 주 대각선, 좌상단에서 우하단
    if all(bingo[i][i]==0 for i in range(5)):
        temp+=1
    

    #대각선2, 부 대각선, 우상단에서 좌하단
    if all(bingo[i][4-i]==0 for i in range(5)):
        temp+=1
    
    return temp

bingo=[list(map(int,sys.stdin.readline().strip().split())) for _ in range(5)]
#2차원 배열을 선언한다
speaker=[] #사회자에 대한 1차원 배열을 선언한다

for _ in range(5):
    speaker+=list(map(int,sys.stdin.readline().strip().split()))

for idx in range(25):
    found = False
    number = speaker[idx]
    
    for x in range(5):
        for y in range(5):
            if bingo[x][y] == number:
                bingo[x][y] = 0
                found = True
                break
        if found:
            break
    
    # 3빙고 확인
    result = check()
    if result >= 3:
        print(idx + 1)
        break