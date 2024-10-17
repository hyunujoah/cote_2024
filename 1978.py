import sys
n=int(sys.stdin.readline().strip())
numbers=list(map(int,sys.stdin.readline().strip().split()))
result=0

for number in numbers: #num은 각 반복 단계마다 nums 리스트의 요소를 나타낸다
    count=0
    if number>1:
        for i in range(2,number):
            if number%i==0:
                count+=1
        if count==0:
            result+=1

print(result)