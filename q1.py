N = int(input())
for case in range(N):
    key = input()
    inp = input()
    if len(key)>len(inp):
        print("Case #%d: IMPOSSIBLE"%(case+1) )
        continue
    A = set(list(key))
    B = set(list(inp))
    if len(inp) == len(key) and (A != B):
        print("Case #%d: IMPOSSIBLE"%(case+1) )
        continue
    if A not in B and (A != B):
        print("Case #%d: IMPOSSIBLE"%(case+1) )
        continue
    
    inp = list(inp)
    key = list(key)
    check = inp.copy()
    for i in (key) :
        inp.remove(i)
    for i in inp :
        check.remove(i)
    if check == key :
        count = (len(inp)) 
        print("Case #%d: %d"%(case+1,count) )
    else :
        print("Case #%d: IMPOSSIBLE"%(case+1) )



