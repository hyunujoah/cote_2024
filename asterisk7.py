import sys
n=int(sys.stdin.readline().strip())
for i in range(1,n):
    print(' '*(n-i)+'*'*(2*i-1))
for i in range(n,0,-1): #n부터 1까지가 범위
    print(' '*(n-i)+'*'*(2*i-1))
