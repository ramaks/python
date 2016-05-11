n=2**1000
print n
y=0
res=0
x=str(n)
for i in range(0,len(x)):
    if(x[i]=='1'):
        y=1
    elif(x[i]=='2'):
        y=2
    elif(x[i]=='3'):
        y=3
    elif(x[i]=='4'):
        y=4
    elif(x[i]=='5'):
        y=5
    elif(x[i]=='6'):
        y=6
    elif(x[i]=='7'):
        y=7
    elif(x[i]=='8'):
        y=8
    elif(x[i]=='9'):
        y=9
    else:
        y=0
    res=sum((res,y))    
print res   
