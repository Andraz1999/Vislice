import bottle
import model
SKRIVNI_KLJUC = 'Zadnji teden predavanj!'

vislice = model.Vislice('stanje.json')
#
##testiranje
#id_testne_igre = vislice.nova_igra()
#(testna_igra, poskus) = vislice.igre[id_testne_igre]
#
##testni


@bottle.get('/')
def prva_stran():
    return bottle.template('index.tpl')


@bottle.post('/nova_igra/')
def zacni_novo_igro():
    # naredi novo igro in preusmeri na nov naslov
    id_igre = vislice.nova_igra()
    bottle.response.set_cookie('id_igre', id_igre, secret=SKRIVNI_KLJUC, path='/')
    
    bottle.redirect('/igra/')
    
    return 


@bottle.get('/igra/')
def prikazi_igro():
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    (igra, poskus) = vislice.igre[id_igre]
    return bottle.template(
        'igra.tpl', igra = igra ,
        id_igre = id_igre,
        poskus = poskus
        )

@bottle.post('/igra/')
def ugibaj_crko():
    crka = bottle.request.forms.getunicode('poskus')
    id_igre = bottle.request.get_cookie('id_igre', secret=SKRIVNI_KLJUC)
    vislice.ugibaj(id_igre, crka)
    bottle.redirect('/igra/')















bottle.run(debug=True, reloader=True)
