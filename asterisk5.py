import sys
n=int(sys.stdin.readline().strip())

for i in range(1,n+1): #1부터 n까지
    print(' '*(n-i)+'*'*(2*i-1))