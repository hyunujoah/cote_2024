#import math를 이용해서 최소공배수, 최대공약수를 구하는 코드

import sys
import math
a,b=map(int,sys.stdin.readline().strip().split()) #두개의 정수를 입력받는, map을 이용하여 맵핑하는

gcd=math.gcd(a,b)
print("최대공약수",          gcd)

lcm=math.lcm(a,b)
print("최소공배수",          lcm)



def gcd(a,b): #a가 3 b가 4라고 가정
    while(b>0):
        a, b = b, a%b #a에는 b라는 값을 대입, b에는 a를 b라는 값으로 나눈 나머지
    return a

def lcm(a,b): #a가 3 b가 4라고 가정
    return a*b//gcd(a,b) #3*4//1

print(gcd(a,b), lcm(a,b))
