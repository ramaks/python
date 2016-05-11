num=3
i=5
a=[]*10001
a[0]=2
a[1]=3
a[2]=5
while(num<10001):
    x=1
    i+=1
    for n in range(0,num):
        if a[n]>0:
            if(i%a[n]):
                pass
            else:
                for j in range(5,i/2):
                    if i%j==0:
                        x=0
                if x==1:
                    a[num]=i
                    num+=1
                    
print i
