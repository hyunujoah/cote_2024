import sys
n=int(sys.stdin.readline().strip())

for i in range(n):
    star='*'*(n-i)
    print(star.rjust(n)) #오른쪽으로 정렬하고 주어진 너비만큼 공백 문자를 채워준다