import sys
num=int(sys.stdin.readline().strip())
temp=num
count=0

while True:
    a=temp//10 #십의 자리 숫자를 출력
    b=temp%10 #일의 자리 숫자를 출력
    c=(a+b)%10 #일의 자리 숫자를 출력
    temp=(b*10)+c

    count+=1
    if(temp==num):
        break

print(count)