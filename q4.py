N = int(input())
for case in range(N) :
    limits = list(map(int,input().split(" ")))
    def digits(n):
        digits = []
        while n !=0 :
            digits.append(n%10)
            n = n//10
        return digits
    count = 0
    for i in range(limits[0],limits[1]+1):
        prod = 1
        dig = digits(i)
        for j in dig :
            prod *= j
        if(prod%sum(dig) == 0):
            count +=1

    print("Case #%d: %d"%(case+1,count))
            