vstup = list(input().split())
# "5 11 2 101 7"
# ["5", "11", "2", "101", "7"]
numbers = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def convert (num, base, numbers):
    num = list(num)
    for i in range(len(num)):
        num[i] = numbers.index(num[i])
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i])*(base**i)
    return decimal

def convertback(num, base, numbers):
    if num == 0:
        return "0"
    result = ""
    while num > 0:
        result = numbers[num % base] + result
        num //= base
    return result
       
num1 = convert(vstup[1][::-1], int(vstup[0]), numbers) #6
num2 = convert(vstup[3][::-1], int(vstup[2]), numbers) #5
base = int(vstup[4])

print(convertback(num1+num2, base, numbers))

sub = num1 - num2
if sub < 0:
    sub = abs(sub)
    print("-"+convertback(sub, base, numbers))
else:
        print(convertback(sub, base, numbers))

print(convertback(num1*num2, base, numbers))

print(convertback(num1 // num2, base, numbers))








