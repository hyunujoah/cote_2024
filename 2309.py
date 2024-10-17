import sys
list_h=[] #리스트 정의
not_nan=[] #리스트 정의
for _ in range(9): #0부터 8, 총 9번을 반복한다
    h=int(sys.stdin.readline().strip())
    list_h.append(h)

list_h.sort()
total=sum(list_h)


for i in range(9):
    for j in range(i+1,9): 
        
        if total-list_h[i]-list_h[j]==100: #총합에서 빼준다
            #9명 중 2명을 뽑아 그 2명 키의 합을 전체 키에서 빼준 값이 100
            not_nan.append(list_h[i])
            not_nan.append(list_h[j])
        if(len(not_nan)==2):
            continue #2개면 스킵

for i in list_h:
    if i in not_nan:
        continue #list_h중에서 not_nan에 해당되면
    print(i)