def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동"%(disk_num, start_peg, end_peg))

def hanoi(n, start_peg, end_peg, mid_peg):
    if n==1:
        move_disk(1,start_peg, end_peg)
    else:
        hanoi(n-1,start_peg, mid_peg,end_peg)
        move_disk(n, start_peg, end_peg)
        hanoi(n-1,mid_peg,end_peg,start_peg)

hanoi(3,1,2,3)