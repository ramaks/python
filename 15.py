x=0
n=20
n+=1
a=[[1 for i in range(n)] for j in range(n)]

for i in range(1,n):
    for j in range(0,n):
        if i==j:
            a[i][j]=a[i-1][j]*2
        else:
            a[i][j]=a[i][j-1]+a[i-1][j]
print a[n-1][n-1]           
