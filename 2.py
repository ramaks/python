##n=100
##x=[0]*n
##x[0]=1
##x[1]=2
##sum1=0
##count=0
##for i in range(0,n):
##    x[i+2]=x[i]+x[i+1]
##    if(x[i]<4000000):
##        if (x[i]%2==0):
##            sum1=sum1+x[i]
##            print sum1
##    else:
##        break
##print x
###########################################
#Method-2
n=100
#x=[0]*n
x1=1
x2=2
x=0
sum1=0
for i in range(0,n):
    
    if(x>4000000):
        break
    if (x%2==0):
        sum1+=x
    print x
    x=x1+x2
    x1=x2
    x2=x
    
print x+2
