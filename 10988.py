import sys
#슬라이싱 기법
#기본 형태 a[start:end:step]
#특정 시작위치부터 끝까지 가져오기, a[start:]
#시작점부터 특정 위치 전까지 가져오기, a[:end]
#특정 위치부터 특정 위치까지 모두 가져오기. a[start:end]
#a[start:end:step], step이 양수일 때 오른쪽으로 step만큼 이동
#step이 음수일 때, 왼쪽으로 step만큼 이동
#a = ['a', 'b', 'c', 'd', 'e']
#전체를 거꾸로 가져온다
#a[ : : -1 ]
#['e', 'd', 'c', 'b', 'a']
#https://twpower.github.io/119-python-list-slicing-examples 참고

test_word=sys.stdin.readline().strip()

if test_word==test_word[::-1]:
    print(1) #숫자 1과 문자 '1'은 다르다
else:
    print(0)