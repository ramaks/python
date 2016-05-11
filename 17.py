str1=['one','two','three','four','five','six','seven','eight','nine']
str2=['eleven', 'twelve',' thirteen', 'fourteen',' fifteen', 'sixteen',' seventeen', 'eighteen', 'nineteen']
str3=['ten','twenty','thirty','forty','fifty', 'sixty',' seventy', 'eighty', 'ninety']
str4=['hundred']
str5=['thousand']
str6=['and']
x=len(str1)
tot=0
tot1=0
tot2=0
tot3=0
tot4=len(str4)
tot5=len(str5)
tot6=len(str6)
tot7=0
for i in range(0,x):
    y=len(str1[i])
    tot1+=y
x=len(str2)    
for i in range(0,x):
    y=len(str2[i])
    tot2+=y
x=len(str3)    
for i in range(0,x):
    y=len(str3[i])
    tot3+=y
for i in range(1,x):
    y=len(str3[i])
    tot7+=y    
tot1=tot1*90
tot2=tot2*10
tot3=tot3*10
tot4=tot4*9
tot6=tot6*99*9
tot7=tot7*90
tot=tot1+tot2+tot3+tot4+tot6+tot5+tot7
print tot



