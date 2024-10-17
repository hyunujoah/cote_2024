import sys
n=int(sys.stdin.readline().strip())
for i in range(n,0,-1): #n부터 시작하여 1까지의 정수를 1씩 감소하여 생성하되, 0은 포함되지 않는 범위를 나타낸다
    print(' '*(n-i)+'*'*(2*i-1))