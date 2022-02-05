class ExamException(Exception):
    pass

def compute_avg_monthly_difference(lista, start=None, end=None):
    #inizio controlli

    #if start is not None and end is not None:
        #controllo l'anno iniziale (start)
        #1 type
        #if not isinstance(start, int):
        #    raise ExamException('TypeError, start = '+ start +' non è un intero ma è di tipo '+ type(start))
        #2 segno
        #if start<0:
        #    raise ExamException('Error, start è negativo')
                 
        #controllo l'anno finale (end)
        #1 type
        #if not isinstance(end, int):
        #    raise ExamException('TypeError, end = '+ end +' non è un intero ma è di tipo '+ type(end))
        #2 segno
        #if end<0:
        #    raise ExamException('Error, end è negativo')

        #3 controllo ordine
        #if start>end:
        #    raise ExamException('Error, forse hai invertito start e end, start non può essere maggiore di end')

    #inizio funzione
        lista_finale = []
        media = 0
        list_anno = []
        for el in lista:
            elem = el[0].split('-')
            if elem[0] == start:
                list_anno.append(el[1])
    
        return list_anno
        #for el in lista:
                    

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
        my_file = open(self.name, 'r')

        for line in my_file:
            #split gli elementi 
            elements = line.split(',')

            #aggiungo ogni lista nella lista finale
            if elements[0] != 'date':
                finish_list.append(elements)  

        #chiudo il file e return la lista di liste
        my_file.close()
        return finish_list 

time_series_file = CVSTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data() 
#print(time_series) 

media = compute_avg_monthly_difference(time_series, '1949', '1951')
print(media)