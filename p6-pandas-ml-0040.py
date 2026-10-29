import pandas as pd
import numpy as np

serie_amigos=["pedro","morgan","farfan","el adrian","jesse","eliseo","mario"]
print("---- Serie listado de amigos NC 0040")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
print("---- Serie listado valor de billetes NC 0040")
amigos = pd.Series(serie_billetes)
print(amigos)

serie_billetes = [20, 50, 100, 200, 500, 1000]
serie_bletras = ["veinte", "cincuenta", "cien", "doscientos", "quinientos", "mil"]
print("---- Serie listado nombre y valor de billetes MX NC 0040")
tablabilletes = pd.Series(serie_billetes, index=serie_bletras)
print(tablabilletes)
# diccionario dataframe
# diccionario de valor de monedas y nombre
print("datos de diccionario a dataframe en pandas")
dic_monedas = {
    "serie_billetes": [20, 50, 100, 200, 500, 1000], 
    "serie_bletras": ["veinte", "cincuenta", "cien", "doscientos", "quinientos", "mil"]
}
tablabilletes = pd.DataFrame(dic_monedas,index=["a","b","c","d","e","f"])
print(tablabilletes)
print("casa de cambio Hugo Fabian NC 0040")