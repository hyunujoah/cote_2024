import sys
#해당 문제 해설 및 풀이
#1.주어진 세점의 x좌표와 y좌표를 각각 따로 리스트에 저장한다
#2.각 좌표의 빈도를 확인하여 축에 평행한 직사각형을 만들기 위한 네번째 점을 찾는다

#예를 들어 세 점이 (1,1),(1,3),(3,1)로 주어졌을 때, 각각의 x,y를 따로 저장
#x좌표 리스트:[1,1,3]
#y좌표 리스트:[1,3,1]

#축에 평행한 직사각형을 만들기 위해서는 각 좌표의 빈도가 홀수인 좌표를 찾아야한다
#위의 예시에서는 x좌표 리스트에서 3이 홀수번 등장하고, y좌표 리스트에서 3이 홀수번 등장한다
#따라서 네번째 점은 (3,3)이 된다

x_coordinates=[]
y_coordinates=[]

for i in range(3):
    x,y=map(int,sys.stdin.readline().strip().split())
    x_coordinates.append(x)
    y_coordinates.append(y)

for i in range(3):
    if x_coordinates.count(x_coordinates[i])==1:
        x=x_coordinates[i]
    if y_coordinates.count(y_coordinates[i])==1:
        y=y_coordinates[i]

print(x,y)