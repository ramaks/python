import math
e=1
for a in range(1,300):
    for b in range(1,500):
        if(b>a):
            c2=a*a+b*b
            c=math.sqrt(c2)
            d=a+b+c
            if(d==1000):
                e=a*b*c
                break
print e    
