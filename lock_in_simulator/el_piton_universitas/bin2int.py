def bin2int(bin):
    n = 0
    for i in range(len(bin)):
        n = n*2+int(bin[i])
    return n
print(bin2int(input()))
