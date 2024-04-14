def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n > 0 y m > 0.
    Devuelve: La distancia binaria entre n y m.
    '''
    i:int = 0
    distance:int = 0
    bin_n:str = bin(n).replace('0b','')
    bin_m:str = bin(m).replace('0b','')

    if len(bin_n) < len(bin_m):
        bin_n = ('0' * (len(bin_m) - len(bin_n))) + bin_n
    elif len(bin_m) < len(bin_n):
        bin_m = ('0' * (len(bin_n) - len(bin_m))) + bin_m

    while i < len(bin_n):
        if bin_n[i] != bin_m[i]:
            distance += 1
        i += 1
    return distance

print(distancia_binaria(12,32))


def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n y m > 0.
    Devuelve: un bool que determina si la distancia entre los dos es 1 o no.
    '''
    isVecinos:bool = False
    distance:int = distancia_binaria(n,m)

    if distance != 1: isVecinos = False
    else: isVecinos = True
    return isVecinos

        


def aledaños_menores(n:int) -> list[int]:
    '''
    completar docstring
    '''


def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    completar docstring
    '''


def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    completar docstring
    '''

