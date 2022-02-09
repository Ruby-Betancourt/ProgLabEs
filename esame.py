from datetime import datetime

class ExamException(Exception):
    pass                  

class CVSTimeSeriesFile():
    #inizializzo la classe
    def __init__(self, name):
        self.name = name
        
        #controllo che sia una stringa
        if not isinstance(self.name, str):
            raise ExamException('TypeError, il nome "{}" non è una stringa'. format(self.name))


    def get_data(self):
        #inizializzo la futura lista di liste
        finish_list = []

        #provo ad aprire il file
        try:
            my_file = open(self.name, 'r')
        except:
            #in caso non riesca ad aprire il file
            raise ExamException('NotFoundError, file non esiste o non è legibile')    

        for line in my_file:
            #separo la stringa sulla virgola 
            elements = line.split(',')
 
            #elimino il carattere '\n'
            elements[-1] = elements[-1].strip()

            if elements[0] != 'date':
                #controllo che i dati passeggeri si possano trasformare in intero
                if not elements[1].isdigit():
                    raise ExamException('Error, {} non è un numero velodo per la media'. format(elements[1]))

                #trasformo tutti i dati del passeggeri in int
                elements[1] = int(elements[1])
                #aggiungo ogni lista nella lista finale
                finish_list.append(elements)  


        #chiudo il file e return la lista di liste
        my_file.close()
        return finish_list 



def compute_avg_monthly_difference(lista, start, end):
    #controlli sull'anno iniziale (start) e finale (end)

    #controllo che siano una stringa
    if not isinstance(start, str):
        raise ExamException('TypeError, l\'anno iniziale non è una stringa')

    if not isinstance(end, str):
        raise ExamException('TypeError, l\'anno finale non è una stringa')

    #controllo che non siano una stringa vuota
    if start == '':
        raise ExamException('Error, l\'anno iniziale è una stringa vuota')

    if end == '':
        raise ExamException('Error, l\'anno finale è una stringa vuota')

    #controllo che siano una stringa di solo numeri
    if not start.isdigit():
        raise ExamException('Error, l\'anno iniziale non è un numero intero')

    if not end.isdigit():
        raise ExamException('Error, l\'anno finale non è un numero intero')    


    #trasformo le date in interi
    start=int(start)
    end=int(end)


    #controllo che siano compresi nel file 
    if start<1949:
        raise ExamException('Error, l\'anno iniziale non compare nel file')

    if end>1960:
        raise ExamException('Error, l\'anno finale non compare nel file')

    #controllo che l'ordine delle date sia giusto
    if start>end:
        raise ExamException('Error, forse hai invertito start e end, start non può essere maggiore di end')


    #inizio funzione
    lista_finale = []
    tot_anni = end-start
    passengers = []
    somma=0
    m=1

    #creo una lista per ogni anno che devo considerare    
    for i in range (tot_anni+1):
        lista_anno = []
        #il primo elemento di ogni lista è l'anno 
        lista_anno.append(start+i)
        passengers.append(lista_anno)

    #riempo le liste con i dati dei passeggeri     
    for data in passengers:
        for item in lista:
            elem = item[0].split('-')
            #solo se l'anno corrisponde all'anno nella lista i dati vengono aggiunti
            if int(elem[0]) == data[0]:
                data.append(item[1])  

    #controlli sui dati dei passeggeri
    for item in passengers:
        for element in item:
            

    #calcolo la media per ogni mese
    while m<=12:
        for y in range(tot_anni):

            diff = passengers[y+1][m]-passengers[y][m]
            somma+=diff
        lista_finale.append(somma/tot_anni)
        somma=0
        m+=1    

    return lista_finale



time_series_file = CVSTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data() 
#print(time_series) 

media = compute_avg_monthly_difference(time_series, '1949', '1951')
print(media) 