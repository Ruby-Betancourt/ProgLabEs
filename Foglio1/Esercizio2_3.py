class CSVFile():
    def __init__(self, name):
        self.name=name

    def get_data(self):
        #inizializzo la lista dove mettere le date
        my_file = open(self.name, 'r')
        
        finish_list = []

        for line in my_file:
            #split gli element 
            elements = line.split(',')
            #aggiungo ogni lista nella lista finale
            if elements[0] != 'Date':
                finish_list.append(elements) 

        my_file.close()
        return finish_list        

from datetime import datetime

class DateCSVFile(CSVFile):
    pass
    def get_data (self):
        data = super().get_data()
        
        fin_list=[]

        #apro il file che mi serve
        file = open(self.name, 'r')

        #per ogni riga 
        for line in file:
            #splito gli elementi
            el = line.split(',')

            #ignoro la prima riga del file
            if el[0]!='Date': 
                my_date = datetime.strptime (el[0], '%d-%m-%Y')
                #aggiungo el[0] alla lista
                fin_list.append(my_date)
                print(my_date.strptime(el[0], '%d-%m-%Y')) 

        #chiudo il file
        file.close()
        #ritorno la lista
        return fin_list

#Esercizio3
    def get_data_vendite(self):
        my_file = open(self.name, 'r')
        
        date_sold = []

        for line in my_file:
            #split gli element 
            elements = line.split(',')
            #aggiungo ogni lista nella lista finale
            if elements[0] != 'Date':
                date_sold.append(elements[0]) 

        my_file.close()
        return date_sold 

    def __str__(self):
        my_file = open(self.name, 'r')
        
        intestazione = []

        for line in my_file:
            element = line.split(',')
            if element[0] == 'Date':
                intestazione.append(element) 

        my_file.close()
        return intestazione

date_vendite = DateCSVFile('shampoo_sales.csv')  
print(date_vendite.__str__())    
    