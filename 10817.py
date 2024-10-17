import sys
numbers=list(map(int,sys.stdin.readline().strip().split()))
numbers.sort()
print(numbers[1])

#abs(): 절댓값해주기 참고