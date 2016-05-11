##import math
##n=6
##x=math.log10(n)
##y=math.log10(x)
##p=n*(x+y-1+(y-2)/x-(y*y-6*y+11)/(2*x*x))
###p=n*(x+y)
##print p
import time
num=3
i=5
start=time.clock()
while(num<10001):
    x=1
    i+=1
    if(i%2==0)or(i%3==0)or(i%5==0):
        pass
    else:
        for j in range(5,i/2):
            if i%j==0:
                x=0
        if x==1:        
            num+=1        
print i
print time.clock()-start
