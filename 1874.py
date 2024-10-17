#스택 수열
import sys
def make_stack_sequence(goal_sequence):
    stack=[]
    commands=[]
    current=1

    for number in goal_sequence:
        while current<=number:
            stack.append(current)
            commands.append('+')
            current+=1
            
        if stack[-1]==number:
            stack.pop()
            commands.append('-')
        
        else:
            return "NO"
    
    return commands

test_number=int(sys.stdin.readline().strip())
goal_sequence=[int(sys.stdin.readline().strip()) for _ in range(test_number)]

print('\n'.join(make_stack_sequence(goal_sequence)))