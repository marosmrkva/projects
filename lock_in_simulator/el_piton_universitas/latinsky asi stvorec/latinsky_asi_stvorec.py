r = input().split()
n = len(r)
square = []
square.append(r)

for i in range(n - 1):
    square.append(input().split())

for i in range(len(square)):
    for j in range(len(square[i])):
        square[i][j] = int(square[i][j])

def find0(line, linenum):
    for j in range(n):
        if line[j] == "0":
            print("chuj w dupe", linenum+1, j+1)

def linecheck(line, linenum):
    n = 0
    linenum = linenum
    for i in range(len(line)):
        if (i+1) in line:
            n += 1
            if line.count(i+1) > 1:
                print("ctverec neni latinsky")
                quit
    if n == len(line):
        return True
    else: 
        find0(line, linenum)
        return False


for i in range(len(square)):
    print("line", linecheck(square[i], i+1))
