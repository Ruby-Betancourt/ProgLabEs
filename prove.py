lista=[]
start = 1949
end = 1951
t=end-start

for i in range (t+1):
    lis = []
    lis.append(start+i)
    lista.append(lis)

i=1
j=t+1
while i<=12:
    while j>=0:
        diff = temp[j][i]-temp[j-1][i]
        somma+=diff
        j-=1
    media.append(somma/t)
    i+=1

i=1
while i<=12:
    for j in range(t+1):
         



listaa = [1949, 2,4,5]
listab = [1950, 5,6,7]
listac = [1951, 7,8,9]

som = 0
c = end
while c!=0:
    
    diff=listac[1]-listab[1]
    c-=1

print (len(listaa))
