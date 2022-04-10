N = int(input())
for _ in range(N):
    n = int(input())
    key = list(map(int,input().split(" ")))
    key = sorted(key)
    i = 1
    count = 0
    while(len(key) != 0):
        mid = int(len(key)/2)
        if i >= key[mid] :
            key = key[mid:len(key):1]

        if i <= key[0]:
            count += 1
            i += 1
        key.pop(0)
    print("Case #%d: %d"%(_+1,count))