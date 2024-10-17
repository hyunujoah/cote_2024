import sys #시간단축
first_number=int(sys.stdin.readline().strip()) #첫번째 입력
second_number=int(sys.stdin.readline().strip())#두번째 입력

print(first_number*(second_number%10))

print(first_number*(second_number%100//10))

print(first_number*(second_number//100))

print(first_number*second_number)