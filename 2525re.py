import sys
hour,minute=map(int,sys.stdin.readline().strip().split()) #split으로 구분하여 입력을 두개 받는다
#(0시부터 23시) (0분부터 59분)
#예를 들어 14 30
duration=int(sys.stdin.readline().strip()) #요리하는 데 필요한 시간
#예를 들어 80
#필요한 시간-예를 들어()

#우선적으로 계산 수행
hour+=duration//60 #예를들어 duration이 50이면 0, 70이면 1
minute+=duration%60 #예를들어 duration이 50이면 50, 70이면 10

#개별적인 조건(분 따로, 시 따로)
if minute>=60: #위에 계산한 결과가
    hour+=1
    minute-=60 #위에 계산한 결과가
if hour>=24:
    hour-=24

print(hour,minute)