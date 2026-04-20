def kombinacie(k, n):
    def komb(i):
        if i == k+1:
            print(c[1:])
        else:
            for j in range(c[i-1]+1, n-k+i+1):
                c[i] = j
                komb(i+1)

    c = [0]*(k+1)
    komb(1)

kombinacie(2, 5)