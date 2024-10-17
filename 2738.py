import sys
#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 코드
#N은 행, M은 열

#예제 입력:
#3 3
#1 1 1
#2 2 2
#0 1 0
#3 3 3 
#4 4 4
#5 5 100

#해당 문제는 리스트 컴프리헨션으로 2차월 배열을 풀게되면 복잡할 수 있다
#리스트 안에 리스트를 넣는다
N,M=map(int,sys.stdin.readline().strip().split())

#두개의 행렬 입력 받기
matrix1=[]
for _ in range(N):
    line=list(map(int,sys.stdin.readline().strip().split()))
    matrix1.append(line)

matrix2=[]
for _ in range(N):
    line=list(map(int,sys.stdin.readline().strip().split()))
    matrix2.append(line)

#두개의 행렬의 합 구하기
_sum=[]
for i in range(N):
    line_sum=[]
    for j in range(M):
        line_sum.append(matrix1[i][j]+matrix2[i][j])
    _sum.append(line_sum)

for value in _sum:
    print(*value)