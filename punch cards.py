from ast import Pass


N = int(input())
for _ in range(N):
    case = list(map(int,input().split(" ")))
    row = case[1]
    ender = []
    for i in range(2*row+1):
        if i%2 == 0 :
            ender.append("+")
        else :
            ender.append("-")
    cont = []
    for i in range(2*row+1):
        if i%2 == 0 :
            cont.append("|")
        else :
            cont.append(".")
    col = case[0]
    table = []
    for j in range(2*col+1):
        if j%2 == 0:
            table.append(ender.copy())
        else :
            table.append(cont.copy())
    for i in range(2):
        for j in range(2):
            table[i][j] = "."

    print("Case #%d:"%(_+1))
    for i in table :
        for j in i :
            print(j,end = "")
        print("\n",end = "")
