
import model

def izpis_igre(igra):
    pravilni_del = igra.pravilni_del_gesla()
    napacne_crke = igra.napacne_crke()
    stevilo_napak = igra.stevilo_napak()
    if stevilo_napak == 0:
        risba = ''
    elif stevilo_napak == 1:
        risba = '\n\n\n\n\n      ________ '
    elif stevilo_napak == 2:
        risba = (
            '            \n'
            '       |    \n'
            '       |    \n'
            '       |    \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 3:
        risba = (
            '       _____\n'
            '       |    \n'
            '       |    \n'
            '       |    \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 4:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |    \n'
            '       |    \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 5:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |    \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 6:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |   | \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 7:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |  /| \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 8:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |  /|\\ \n'
            '       |    \n'
            '      _|______ '
        )
    elif stevilo_napak == 9:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |  /|\\ \n'
            '       |  /  \n'
            '      _|______ '
        )
    elif stevilo_napak == 10:
        risba = (
            '       _____\n'
            '       |   | \n'
            '       |   o \n'
            '       |  /|\\ \n'
            '       |  / \\\n'
            '      _|______ '
        )

    tekst =(
        f'{risba}\n'
        f'===================\n\n'
        f'{pravilni_del}\n'
        f'Napačne črke so: {napacne_crke}\n'
        f'Število napak {stevilo_napak}/{model.STEVILO_DOVOLJENIH_NAPAK}\n\n'
        f'==================='
    )
    return tekst




def izpis_zmage(igra):
    niz = 'Rešil si do sedaj najtežjo besedo!'
    return niz

def izpis_poraza(igra):
    niz = f'Včasih pač pride "štk", pravilno geslo je {igra.geslo}, poskusi še enkrat...'
    return niz

def zahtevaj_vnos():
    vnos = input('Poskusi uganit črko: ')
    return vnos

#def preveri_vnos(vnos):
#    '''Funkcija vrne True, če je izraz primeren, sicer vrne False'''
#    if len(vnos) == 1:
#        print('Neveljaven vnos. Ne se zafrkavat')
#        return False
#    else:
#        return True


def zazeni_vmesnik():
    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))

        poskus = zahtevaj_vnos() 
        
#        if not preveri_vnos(poskus):
#            continue

        rezultat = igra.ugibaj(poskus)
        # preverimo, če je igre konec
        if igra.poraz():
            print(izpis_igre(igra))
            print(izpis_poraza(igra))
            return

        elif igra.zmaga():
            print(izpis_igre(igra))
            print(izpis_zmage(igra))
            return

    return
#poženemo program
zazeni_vmesnik()