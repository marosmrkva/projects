hexadecimal = input()[::-1]
decimal = 0
for i in range(len(hexadecimal)):
    decimal += (int(hexadecimal[i])*(16**i))

print(decimal)