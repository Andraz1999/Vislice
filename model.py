# Definiramo konstante

STEVILO_DOVOLJENIH_NAPAK = 10

PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = '0'
NAPACNA_CRKA = '-'

ZACETEK = 'S'
ZMAGA = 'W'
PORAZ = 'X'

# definiramo logicni model igre

class Igra:
    
    def __init__(self, geslo, crke):
        self.geslo = geslo # string
        self.crke = crke  # list
        return

    def __repr__(self):
        return f'Igra({self.geslo}, {self.crke})'

    def napacne_crke(self):
        seznam = []
        for i in self.crke:
            if i not in self.geslo:
                seznam.append(i)
        return seznam

    def pravilne_crke(self):
        seznam = []
        for i in self.crke:
            if i in self.geslo:
                seznam.append(i)
        return seznam

    def stevilo_napak(self):
        seznam = self.napacne_crke()
        return len(seznam)

    def zmaga(self):
        for i in self.geslo:
            if i not in self.crke:
                return False
        return True

    def poraz(self):
        if self.stevilo_napak() >= STEVILO_DOVOLJENIH_NAPAK:
            return True
        else:
            return False

    def pravilni_del_gesla(self):
        niz = ''
        for i in self.geslo:
            if i in self.crke:
                niz += ' ' + i
            else:
                niz += ' _'
        return niz.strip()  #počistimo presledke

    def nepravilni_ugibi(self):
        niz = ''
        for i in self.napacne_crke():
            niz += (i + ' ')
        return niz.strip()

    def ugibaj(self, n):
        n = n.upper()
        if n in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(n)
            if self.zmaga():
                return ZMAGA
            elif self.poraz():
                return PORAZ
            elif n in self.geslo:
                return PRAVILNA_CRKA
            else:
                return NAPACNA_CRKA

        
with open('besede.txt', 'r', encoding='UTF-8') as vhod:
    read = vhod.read()
    read = read.split('\n')
    bazen_besed = tuple(read) 

def nova_igra():
    import random
    geslo = random.choice(bazen_besed)
    geslo = geslo.upper()
    return Igra(geslo, [])

class Vislice:
    def __init__(self):
        # v slovarju ugre ima vsaka igra svoj ID
        # ID je celo število
        self.igre = {} 
        return
    
    def prost_id_igre(self):
        if self.igre == {}:
            return 0
        else:
            # preverimo katero od prvih n+1 števil
            # še ni uporabljeno za ID 'n' iger 
            for i in range(len(self.igre) + 1):
                if i not in self.igre.keys():
                    return i

    def nova_igra(self):
        # naredi novo igro z naključnim geslom
        igra = nova_igra()
    
        # shrani(ZACETEK, igra) v slovar z novim ID
        id = self.prost_id_igre()
        self.igre[id] = (igra, ZACETEK)
        return id

    def ugibaj(self, id_igre, crka):
        (igra, _) = self.igre[id_igre]
        nov_poskus = igra.ugibaj(crka)
        # shrani rezultat poskusa v slovar
        self.igre[id_igre] = (igra, nov_poskus)
        return

