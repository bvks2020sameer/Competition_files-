N = int(input())
for _ in range(N):
    t = []
    p1 = list(map(int,input().split(" ")))
    p2 = list(map(int,input().split(" ")))
    p3 = list(map(int,input().split(" ")))
    if(sum(p2)<10**6 and sum(p2)<10**6 and sum(p3)<10**6 ):
        print("Case #%d: Impossible"%(_+1))
        break
    else :
        if(sum(p1) == 10**6):
            t.append(sum(p1))
            p1 = [str(i) for i in p1]
            print("Case #%d: %s"%(_+1," ".join(p1)))
        elif(sum(p2) == 10**6):
            t.append(sum(p2))
            p2 = [str(i) for i in p2]
            print("Case #%d: %s"%(_+1," ".join(p2)))
        elif(sum(p3) == 10**6):
            t.append(sum(p3))
            p3 = [str(i) for i in p3]
            print("Case #%d: %s"%(_+1," ".join(p3)))
        else :
           p1 = [str(i) for i in p1]
           print("Case #%d: %s"%(_+1," ".join(p1)))
    