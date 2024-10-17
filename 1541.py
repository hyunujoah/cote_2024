import sys
def min_calculation(math_line):

    separations=math_line.split('-')

    front_sum=sum(map(int,separations[0].split('+')))

    behind_sum=sum(sum(map(int,separation.split('+'))) for separation in separations[1:])

    result=front_sum-behind_sum

    return result

math_line=sys.stdin.readline().strip()

print(min_calculation(math_line))

#예시, 55-50+40-30+20