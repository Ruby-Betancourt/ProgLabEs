class Automobile():
    def __init__(self, casa_automo, modello, numero_posti, targa):
        self.casa_automo = casa_automo
        self.modello = modello
        self.numero_posti = numero_posti
        self.targa = targa

    def __str__(self):
        print('Casa automobilistica: {}'.format(self.casa_automo))
        print('Modello: {}'.format(self.modello))
        print('Numero posti: {}'.format(self.numero_posti))
        print('Targa: {}'.format(self.targa))

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

#Esercizio5
class Transformer(Automobile):
    def __init__(self, nome, grado, generazione, reparto):
        super().__init__(nome, grado, generazione, reparto)
        self.nome = nome
        self.generazione = generazione
        self.grado = grado
        self.reparto = reparto

    def scheda_militare(self):
        print('Nome: {}'.format(self.nome))
        print('Generazione: {}'.format(self.generazione))
        print('Grado: {}'.format(self.grado))
        print('Reparto: {}'.format(self.reparto))


auto = Automobile('toyota', 'yaris', 5, 'GC278YN')
auto2 = Automobile('fiat', 'panda', 5, 'BR382BA')
auto3 = Automobile('toyota', 'yaris', 5, 'KJ912AC') 
#auto.__str__()  
#print(auto.confronta(auto3))     

t_0 = Transformer('Maximus', 3, 'capitano', 'artiglieria pesante')
t_1 = Transformer('Bubble', 1, 'sargente','spionaggio')
#t_1.scheda_militare()

#Esercizio6
#question 
print('Question 1:{}'.format(isinstance(auto, Automobile)))

if issubclass(Transformer, Automobile):
    print('Question 2: La superclasse é Automobile, la sottoclasse é Transformer')

print('Question 3:{}'.format(isinstance(t_0, Transformer)))

if type(t_1)==type(t_0):
    flag=True
else:
    flag=False    
print('Question 4:{}'.format(flag))

if type(auto)==type(t_0):
    flag=True
else:
    flag=False 
print('Question 5:{}'.format(flag))

print('Question 6:{}'.format(isinstance(t_1, Automobile)))

print('Question 7:{}'.format(isinstance(auto, Transformer)))
