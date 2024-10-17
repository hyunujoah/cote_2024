import sys
arr=sys.stdin.readline().strip()
count=[0]*26 #인덱스 0을 a, 1을 b, 2를 c, z를 25로 처리한다

for i in arr:
    count[ord(i)-97]+=1

print(*count)