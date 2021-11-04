import requests

def zapisDb(typ,stav):

    if(typ == "garage"):
        pin = 420420
    if(typ == "gate"):
        pin = 222

    url = "http://nightingales.clanweb.eu/writeNewState.php"
    obj = {'pin': pin, 'stav': stav, 'typ': typ}

    x = requests.post(url, data = obj)

    #print(x.text)