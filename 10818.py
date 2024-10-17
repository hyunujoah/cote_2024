import sys
test_case=int(sys.stdin.readline().strip())
integers=list(map(int,sys.stdin.readline().strip().split()))

max=integers[0]
min=integers[0]

for i in integers[1:]: #슬라이싱 기법
    if i>max:
        max=i
    elif i<min:
        min=i

print(min,max)