from random import shuffle
from collections import namedtuple
Carta = namedtuple("Carta" , ("rango" ,"seme"))

separatore_1 = "_" * 40
separatore_2 = "-" * 40


class MazzoNapoletano:

    ranghi = ['A'] + [str(n) for n in range(2,8)] + "FANTE CAVALLO RE".split(" ")
    semi = "SPADE COPPE BASTONI DENARI".split(" ")

    def __init__(self):
        self.resetta_mazzo()
        return
    

    def resetta_mazzo(self):
        self.carte = [Carta(rango , seme) for seme in self.semi for rango in self.ranghi]
        return
    

    def mischia_carte(self):
        shuffle(self.carte)
        return
    

    def dai_carte(self , numero_di_carte):
        nuova_mano = self.carte[:numero_di_carte]
        self.carte = self.carte[numero_di_carte:]
        return nuova_mano
    
    def __getitem__(self , indice):
        return self.carte[indice]
    def __len__(self):
        return len(self.carte)


    def __str__(self):
        stringa_di_ritorno  = f"carte nel mazzo : {len(self)}\n"
        stringa_di_ritorno += "carte :\n"
        stringa_di_ritorno += "\n".join(self.carte)
        return stringa_di_ritorno
    

    def __repr__(self):
        return str(self)
    


class Giocatore:

    def __init__(self , nome):
        self.resetta_giocatore(nome)
        return
    

    def resetta_giocatore(self , nome):
        self.nome = nome
        self.vittorie  = 0
        self.punteggio = 0
        self.carte_prese = 0
        self.mano = []
    

    def fai_mossa(self):
        print("effettua una mossa: ")
        for numero , carta in range(len(self.mano)) , self.mano:
            print(f"[{numero + 1}] : {carta[0]} di {carta[1]}")
            scelta = int(input(">"))
        mossa = self.mano.pop(scelta - 1)
        return mossa

    
    def calcola_punteggio_attuale(self):
        return 489
    
    def __str__(self):
        stringa_di_ritorno =   separatore_2 + \
                             f"nome : {self.nome}\n" + \
                             f"vittorie : {self.vittorie}\n" + \
                             f"punteggio : {self.punteggio}\n" + \
                             f"carte prese : {self.carte_prese}\n" + \
                               separatore_2
        return stringa_di_ritorno



class Banco:
    def __init__(self):
        self.resetta_banco()
        return
    

    def resetta_banco(self):
        self.mazzetto = None
        self.giocatori = []
        self.carte_sul_banco = {} #il vocabolario è del tipo "nome_del_proprietario" : carta
        self.briscola = None
    

    def aggiungi_mazzo_napoletano(self):
        self.mazzetto = MazzoNapoletano()
        return
    

    def aggiungi_giocatori(self , nuovi_giocatori):
        self.giocatori.append(nuovi_giocatori)
        return
    
    def distribuisci_carte(self):
        for giocatore in self.giocatori:
            giocatore.mano = self.mazzetto.dai_carte(3)
    
    def __str__(self):
        stringa_di_ritorno = f"mazzetto =\n{self.mazzetto}" + \
                               separatore_1 + \
                             f"giocatori:" + ", ".join(self.giocatori) + "\n" + \
                               separatore_1+ \
                             f"carte sul banco:\n" + "||".join(self.carte_sul_banco)
        return stringa_di_ritorno



class Partita:
    def __init__(self , giocatori_nella_partita):
        self.resetta_partita(giocatori_nella_partita)
        return
    

    def resetta_partita(self , giocatori_nella_partita): # i giocatori sono solo nomi , non oggetti
        self.lista_giocatori = giocatori_nella_partita
        self.banco = Banco()
        for giocatore in self.lista_giocatori:
            giocatore = Giocatore(giocatore) #viene creato l'oggetto giocatore
            self.banco.aggiungi_giocatori(giocatore) #il giocatore viene aggiunto al tavolo
        self.banco.aggiungi_mazzo_napoletano() #il mazzo viene aperto
    

    def determina_vincitore_del_turno(self):
        return self.banco.giocatori[0]
    
    def gioca(self):
        self.banco.mazzetto.mischia_carte() # il mazzo viene mischiato
        self.banco.briscola = self.banco.mazzetto.carte[-1]
        if len(self.banco.giocatori) == 3:
            carta_esclusa = self.banco.mazzetto.carte.pop(0)
            while carta_esclusa[1] == self.banco.brsicola[1]: #se escludo una carta devo assicurarmi che non abbia lo stesso seme della briscola
                self.banco.mazzetto.carte.append(carta_esclusa) # rimetti la carta nel mazzo
                self.banco.mazzetto.mischia_carte() # mischia di nuovo le carte
                self.banco.brsicola = self.banco.mazzetto.carte[-1]

        while len(self.banco.mazzetto): #continua a giocare finché il mazzetto non è vuoto
            for giocatore in self.banco.giocatori:
                giocatore.mano = self.banco.mazzetto.dai_carte(3)
            for giocatore in self.banco.giocatori: #ogni giocatore poggia una carta sul banco
                nuova_carta_sul_banco = giocatore.fai_mossa() #una mossa viene chiesta al giocatore , il valore di ritorno è una carta
                self.banco.carte_sul_banco[giocatore] = nuova_carta_sul_banco #la carta viene poggiata sul banco a nome del proprietario
        
        vincitore_del_turno = self.determina_vincitore_del_turno()
        vincitore_del_turno.carte_prese += [self.banco.carte_sul_banco[carta_sul_tavolo]
                                            for carta_sul_tavolo in self.banco.carte_sul_banco]
        
print("hola gringos")


