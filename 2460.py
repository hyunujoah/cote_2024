import sys
passenger=0
max_passenger=0

for _ in range(10): #10개의 역
    out_train, in_train=map(int,sys.stdin.readline().strip().split())
    passenger+=in_train-out_train #각 역에서 현재 기차에 있는 사람보다 더 많은 사람이 내리는 경우는 없다
    max_passenger=max(passenger,max_passenger)

print(max_passenger)