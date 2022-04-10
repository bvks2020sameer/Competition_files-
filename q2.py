N = int(input())
for case in range(N) :
    print
    n = int(input())
    def digits(n):
        digits = []
        while n !=0 :
            digits.append(n%10)
            n = n//10
        return digits
    key = sum(digits(n))
    a = ''
    b = ''
    for i in range(10):
        if ((i+key)%9 == 0):
            a = str(i)+str(n)
            b = str(n) +str(i)
            break

    a = int(a)
    b = int(b)
    res = 0
    if i == 0 :
        res = b
    else :
        if a<b :
            res =a 
        else :
            res = b
    print("Case #%d: %d"%(case+1,res))
