import sys
int(sys.stdin.readline().strip())
a=[i for i in map(int,sys.stdin.readline().strip().split())]
#맵핑을 하고
a.sort() #오름차순
tmp=0
if len(a)%2==1:
    tmp=a.pop(-1)
b=[a[i]+a[-i-1] for i in range(len(a)//2)]
b.append(tmp)

print(max(b))

#PT 첫째 날에 1과 4를 선택하고, 둘째 날에 2와 3을 선택하고, 마지막 날에
#5를 선택하면 M은 5가 되며, 이때가 M이 최소일 때이다.