def stampa(lista):
    print('{}'. format(lista[0:len(lista)]))

def statistiche(a):
    somma=0
    minimo=a[1]
    massimo=a[1]
    for element in a:
        somma+=element
        if minimo>element:
            minimo=element
        if massimo<element:
            massimo=element    
    
    media=somma/(len(a))

    print('somma={}'.format(somma))
    print('media={}'.format(media))
    print('minimo={}'.format(minimo))
    print('massimo={}'.format(massimo))

def somma_vettoriale(a,b):
    #controllo se a è fatta da interi
    count_a=0
    for element in range (len(a)):
        if type(a[element]) is int:
            count_a+=1

    #controllo se b è fatta da interi
    count_b=0
    for element in range (len(b)):
        if type(b[element]) is int:
            count_b+=1

    #stessa dimensione a e b?
    new_list=[]
    if count_a==len(a) and count_b==len(b):
        if len(a)==len(b):
            for el in range (len(a)):
                som=a[el]+b[el]
                new_list.append(som)
    return new_list            


prova=[6,3,1,2,4]
stampa(prova)
statistiche(prova)

test_a=[1,8,3,4,2]
test_b=[4,0,2,1,5]
result=[]
result=somma_vettoriale(test_a, test_b)
stampa(result)
