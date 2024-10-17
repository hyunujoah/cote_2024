import sys #원래 설정되어 있는 알람을 !45분! 앞서는 시간으로 바꾸는 것
hour,minute=map(int,sys.stdin.readline().strip().split()) #split로 구분하여 mapping해서 int로 형변환하여 입력을 받는다

if minute<45:
    if hour==0: #0이 반전이 되는 시간이므로 기준을 0으로 잡는다
        hour==23 #0이 반전이되는 정각이므르 0시에서 45분을 빼면 23시로 된다
        minute+=60
    elif hour!=0:
        hour-=1
        minute+=60

print(hour,minute-45) #45분 앞서서 시간을 바꾸기