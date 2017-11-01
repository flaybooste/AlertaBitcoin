import requests as r

def Mbt(id):
    url = "https://www.mercadobitcoin.net/api/BTC/ticker/"
    if(id==1):
        mbt = r.get(url)
        valorCompra = mbt.json()['ticker']['buy']
        return valorCompra
    if(id==2):
        mbt = r.get(url)
        valorVenda = mbt.json()['ticker']['sell']
        return valorVenda



def Nc(id):
    url = "https://broker.negociecoins.com.br/api/v3/BTCBRL/ticker"
    if(id==1):
        nc = r.get(url)
        valorCompra = nc.json()['buy']
        return valorCompra
    if(id==2):
        nc = r.get(url)
        valorVenda = nc.json()['sell']
        return valorVenda
    
