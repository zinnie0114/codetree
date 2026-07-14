
a=0

for i in range(3):
    sym, temp = input().split()
    temp=int(temp)

    if sym == 'Y' and temp >= 37:
        a+=1
    '''elif sym == 'N' and temp >= 37:
        #print('B')
    elif sym=='Y'and temp < 37:
        #print('C')
    else: 
        #print('D')'''

if a>=2:
    print('E')
else:
    print('N')
