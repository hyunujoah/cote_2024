import sys
n=int(sys.stdin.readline().strip())
def fibo(n):
    if n<=1:
        return n
    return fibo(n-1)+fibo(n-2)

print(fibo(n))

#피보나치 수는 0과 1로 시작한다
#0번재 피보나치 수는 0이고, 1번째 피보나치 수는 1이다