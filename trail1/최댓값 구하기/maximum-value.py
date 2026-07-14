a,b,c = map(int, input().split())

if a>b and a>c:
    if a>c:
        print(a)
    else: 
        print(c)
    
else: 
    if b>c:
        print(b)
    else:
        print(c)