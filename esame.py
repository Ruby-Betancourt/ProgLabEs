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

        #apro il file
        try:
            my_file = open(self.name, 'r')
        except:
            raise ExamException('NotFoundError, file non esiste o non è legibile')    

        for line in my_file:
            #split gli elementi 
            elements = line.split(',')

            #elimino il carattere '\n'
            elements[-1] = elements[-1].strip()

            if elements[0] != 'date':
                #trasformo tutti i dati del passeggeri in int
                elements[1] = int(elements[1])
                #aggiungo ogni lista nella lista finale
                finish_list.append(elements)  


        #chiudo il file e return la lista di liste
        my_file.close()
        return finish_list 



def compute_avg_monthly_difference(lista, start, end):
    #inizio controlli
    
    #controllo che sia una stringa
    #isinstance()

    #controllo che non sia una stringa vuota

    #controllo che sia una stringa di numeri
    #isdigit()

    start=int(start)
    end=int(end)

    #controllo l'anno iniziale (start)
    #1 type
    #if not isinstance(start, int):
    #    raise ExamException('TypeError, start non è di tipo int')
    #2 segno
    #if start<0:
    #    raise ExamException('Error, start è negativo')
             
    #controllo l'anno finale (end)
    #1 type
    #if not isinstance(end, int):
    #    raise ExamException('TypeError, end non è di tipo int')
    #2 segno
    #if end<0:
    #    raise ExamException('Error, end è negativo')

    # controllo che start non sia minore di 1949 cioe la prima data

    #3 controllo ordine
    #if start>end:
    #    raise ExamException('Error, forse hai invertito start e end, start non può essere maggiore di end')



    #inizio funzione
    lista_finale = []
    media = 0
    t=end-start
    temp = []
    somma=0
        
    for i in range (t+1):
        list_anno = []
        list_anno.append(start+i)
        temp.append(list_anno)
        
    #lis_year = []
    #for el in lista:
    #    elem = el[0].split('-')
    #    if int(elem[0]) == start:
    #        lis_year.append(el[1])

        
    for dat in temp:
        for el in lista:
            elem = el[0].split('-')
        
            if int(elem[0]) == dat[0]:
                dat.append(el[1])  

    i=1
    #j=t+1
    while i<=12:
        #while j>=0:
        for j in range(t):
            diff = temp[j+1][i]-temp[j][i]
            #print(temp[j][i])
            #print(diff)
            somma+=diff
            #j-=1
        lista_finale.append(somma/t)
        i+=1    

    return lista_finale



time_series_file = CVSTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data() 
#print(time_series) 

media = compute_avg_monthly_difference(time_series, '1949', '1951')
print(media)