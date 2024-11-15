pais = input('Dime 3 paises que quires visitar: ')
def visitar(pais):
     print('me gustaria visitar', pais)
     return pais
paises = [pais]
lugares = visitar(paises)
print(lugares)

numeros = input('dime una lista de numeros separados con comas: ')
print(min(numeros))
print(max(numeros))