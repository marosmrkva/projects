from math import sqrt, floor
numbers = input().split()

for i in range(len(numbers)):
    count = 0
    current = int(numbers[i])
    
    for j in range(1, int(current/sqrt(2))+1):
        b_sqrd = current**2 - j**2
        b = sqrt(b_sqrd)
        if b == floor(b) and b != 0 and j**2 + b**2 == current**2:
            count += 1

    print(current, count)