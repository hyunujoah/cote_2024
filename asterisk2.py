import sys 
n=int(sys.stdin.readline().strip())
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

for i in range(0,n):
    star='*'*(i+1)
    print(star.rjust(n)) #전체 n에서 오른쪽 정렬을 하는 .rjust(n)을 사용!
    