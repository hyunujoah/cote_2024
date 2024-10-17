import sys
h,m=map(int,sys.stdin.readline().strip().split()) #h,hour m,minute
timer=int(sys.stdin.readline().strip()) #요리하는 데 필요한 시간(타이머)

h+=timer//60 #60으로 나눈 몫
m+=timer%60 #60으로 나눈 나머지, ex)0%60은 0, 20%60은 20, 90%60은 30

#개별적인 조건
if m>=60: #위에서 수행한 연산결과가 m>=60이면
    h+=1
    m-=60 
if h>=24: #위에서 수행한 연산결과가 h>=24이면
    h-=24

print(h,m)