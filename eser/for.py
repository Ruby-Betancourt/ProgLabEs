def media(lista):
    media = []
    somma = 0
    '''for i in range(len(lista)):
       #print(i)
        somma += lista[i]
    return somma/len(lista)'''
    
    for j in range(len(lista)-1+1):
        for i in range(1):
            somma += lista[j+i]
        media.append(somma/1)   
        somma = 0
    return media    

result = media([8,16,4,3,2,43])
print(result)    

media=[0]
#print(type(media[0]))
#print(len(media))
