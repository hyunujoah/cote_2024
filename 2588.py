import sys
first=int(sys.stdin.readline().strip())
second=int(sys.stdin.readline().strip())

print(first*(second%10))

print(first*(second%100//10))

print(first*(second//100))

print(first*second)