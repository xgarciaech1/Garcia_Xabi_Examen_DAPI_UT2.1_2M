def area_cuadrado(lado):
    '''Aqui vamos a calcular el area del cuadrado
    lado ** 2'''
    return lado ** 2
print(area_cuadrado(5))

def mayor_de_tres(a, b, c):
    '''Devolver el numero mas grande
    '''
    if a > b:
        if a > c:
            if c > b:
                print(b, 'menor')
                print(a, 'grande')
            else:
                print(a, 'grande')
                print(c, 'menor')
        else:
            print(c, 'grande')
            print(b, 'menor')
    elif b > c:
        if a > c:
            print(b, 'grande')
            print(c, 'menor')
        else:
            print(b, 'grande')
            print(a, 'menor')