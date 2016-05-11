n=600851475143
num=1
x=0
i=2
j=2
while(i<n):
    if(n%i==0):
        while(j<i):
            if(i%j==0): 
               x=1
               break
            j+=1  
        if(x==0):
            num=i
        print i    
    i+=1        
print num               
               
