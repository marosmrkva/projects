
numbers = [chr(i) for i in range(48, 58)] + [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]


#['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("f", numbers.index("j"))

vstup = input()

def convert (num, base, numbers):
    num = list(num)
    for i in range(len(num)):
        num[i] = numbers.index(num[i])
    print(num)
    decimal = 0
    for i in range(len(num)):
        decimal += int(num[i])*(base**i)
    return decimal

def convertback (num, base, numbers):#11
    out = ""
    while num > base: #num > 7
        out = out + str(numbers[num//base])
        num = num%base
    out = out + str(numbers[num])
    return out #14

decimal = convert(vstup, 11, numbers)
print("11 -> 10:", decimal)
print("10 -> 11:", convertback(decimal, 11, numbers))