from datetime import datetime

lista=[]
start = 1949
t=2
temp=[['1949-01',42],['1949-02',48],['1949-03',10],['1950-01',72],['1950-02',45],['1950-03',90],['1951-01',70],['1951-02',24],['1951-03',18]]


for i in range (t+1):
    lis = [None,None,None]
    lis.append(start+i)
    lista.append(lis)
print(lista)

for data in lista:
    for item in temp:
        elem = item[0].split('-')
        if int(elem[0]) == data[-1]:
            data[int(elem[1])] = item[1]


print(lista)

l=[]
somma=0

m=1
#for m in range(3):
while m<=3:    
    for j in range(t):
        if lista[j+1][m]==None or lista[j][m]==None:
            diff = 0
        else:
            diff = lista[j+1][m]-lista[j][m]
        somma+=diff
    #media = somma/t
       
    l.append(somma/t)
    somma = 0 
    m+=1    
         
print (l)

date1=datetime.strptime(temp[0][0], '%Y-%m')
for item in temp[1:]:
    #contorllo le date
    date_=datetime.strptime(item[0], '%Y-%m')
    #controllo siano crescenti e non si ripetano
    if date1>=date_:
        print('raise error')
    date1 = date_

    
        

