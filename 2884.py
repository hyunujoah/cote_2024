import sys
h,m=map(int,sys.stdin.readline().strip().split())

if m<45:
    if h==0: #시가 0이면
        h=23
        m+=60
    else: #시가 0이 아니면
        h-=1
        m+=60
        
print(h,m-45)