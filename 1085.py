import sys
x,y,w,h=map(int,sys.stdin.readline().strip().split())

print(min(x,y,h-y,w-x))