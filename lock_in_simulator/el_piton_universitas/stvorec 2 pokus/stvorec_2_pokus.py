r = input().split()
#["1", "2", "3"]
n = len(r)
#3
square = []
square.append(r)
#[["1", "2", "3"]]

for i in range(n - 1):
    square.append(input().split())
#[["1", "2", "3"],["1", "2", "3"],["1", "2", "3"]]

for i in range(len(square)):
    for j in range(len(square[i])):
        square[i][j] = int(square[i][j])
#[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

def check (square, n):
    assumedsum = 0
    validlines = 0
    for i in range(n):
        assumedsum += i+1
    for i in range(n): #kontrola riadkov
        numcount = 0
        for j in range(n):
            if  j+1 in square[i] and square[i].count(j+1) == 1:
                numcount += 1
        if numcount != n:
            if 0 in square[i]:
                swapfor0 = assumedsum - sum(square[i])                
                column = []
                for k in range(n):
                    column.append(square[k][square[i].index(0)])
                if sum(column) + swapfor0 == assumedsum:
                    return (f"ctverec lze doplnit na latinsky cislem {swapfor0}")
                else:
                    return("ctverec nelze doplnit na latinsky")
            else:
                return "ctverec neni latinsky"
        else:
            validlines += 1
        if validlines == n:
            for i in range(n): #kontrola stlpcov
                column = []
                numcount = 0
                for j in range(n):
                    column.append(square[j][i])
                for i in range(n):
                    if i+1 in column:
                        numcount += 1
                if numcount != n:
                    return "ctverec neni latinsky"
                else:
                    return "ctverec je latinsky"



print(check(square, n))











