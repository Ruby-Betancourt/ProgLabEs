lista=[]
#start = 1949
#end = 1951
#t=end-start
t=2

#for i in range (t+1):
 #   lis = []
 #   lis.append(start+i)
 #   lista.append(lis)


s='1949-05,'
s1='1949-02'
elements = s1.split(',')
#print(elements)

ti='ciao '
result=ti.isdigit()
print(result)

somma=0
temp=[[1,2,3,4],[1,6,7,8],[1,4,8,10]]
m=1 
while m<=3:
    for j in range(t):
        diff = temp[j+1][m]-temp[j][m]
        #print(temp[j+1][m])
        #print(temp[j][m])
        #print(diff)
        somma+=diff
        #print('somma')
        #print(somma)
    media = somma/t
    #print('media')
    #print(media)    
    lista.append(media)
    m+=1    
         
#print (lista)

