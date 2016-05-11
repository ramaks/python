n=13
longest=25
while(n<1000000):
    n+=1
    x=n
    count=1
    while x!=1:
        count+=1
        if(x%2==0):
            x=x/2
        else:
            x=3*x+1
    if(count>longest):
        longest=count
            
print longest
n=100
while(n<1000000):
    n+=1
    x=n
    count=1
    while x!=1:
        count+=1
        if(x%2==0):
            x=x/2
        else:
            x=3*x+1
    if(count==longest):
        break
print n   
