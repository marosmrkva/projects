vstup = int(input())
binary = ""
hexadecimal = ""

while vstup != 0:
    binary = str((vstup%2)) + binary
    vstup //= 2
while len(binary)%4 != 0:
    binary = "0" + binary

print("binary = ", binary)

for i in range(len(binary)//4):
    bit = ""
    for j in range (4):
        bit = bit + binary[j+(i*4)]
    
    match bit:
        case "0000":
            hexadecimal = hexadecimal + "0"
        case "0001":
            hexadecimal = hexadecimal + "1"
        case "0010":
            hexadecimal = hexadecimal + "2"
        case "0011":
            hexadecimal = hexadecimal + "3"
        case "0100":
            hexadecimal = hexadecimal + "4"
        case "0101":
            hexadecimal = hexadecimal + "5"
        case "0110":
            hexadecimal = hexadecimal + "6"
        case "0111":
            hexadecimal = hexadecimal + "7"
        case "1000":
            hexadecimal = hexadecimal + "8"
        case "1001":
            hexadecimal = hexadecimal + "9"
        case "1010":
            hexadecimal = hexadecimal + "A"
        case "1011":
            hexadecimal = hexadecimal + "B"
        case "1100":
            hexadecimal = hexadecimal + "C"
        case "1101":
            hexadecimal = hexadecimal + "D"
        case "1110":
            hexadecimal = hexadecimal + "E"
        case "1111":
            hexadecimal = hexadecimal + "F"

print("hexadecimal = ", hexadecimal)