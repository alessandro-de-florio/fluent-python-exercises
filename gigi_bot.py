from briscopy import *


class Bot(Giocatore):
    def fai_mossa(self):
        print("vai in mona!")
        print("DEBUG : CAlogero lancia:", end=' ')
        carta_selezionata = self.mano.pop(randint(0, 2))
        print(carta_selezionata)
        return carta_selezionata


Calogero = Bot("Calogero")
Ale = Giocatore("Ale")
gioco = Partita([Ale, Calogero])

diz = {"Calogero": Calogero}
diz["Ale"] = Ale
print(diz)
for roba in diz:
    print(roba)

gioco.gioca()

