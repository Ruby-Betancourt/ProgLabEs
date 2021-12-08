class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    def __str__(self):
        print('{}'.format(self.casa_automo))
        print('{}'.format(self.modello))
        print('{}'.format(self.numero_posti))
        print('{}'.format(self.targa))

    def parla(self):
        print('Broom Broom')    
    
    def confronta(self, self_1):
        count=0
        if self.casa_automo == self_1.casa_automo:
            count+=1
        if self.modello == self_1.modello:
            count+=1
        if self.numero_posti == self_1.numero_posti:
            count+=1
        if count == 3:
            return True
        else:
            return False                
#


auto = Automobile('toyota', 'yaris', 5, 'GC278YN')
auto2 = Automobile('fiat', 'panda', 5, 'BR382BA')
auto3 = Automobile('toyota', 'yaris', 5, 'KJ912AC') 
auto.__str__()  
print(auto.confronta(auto3))     

