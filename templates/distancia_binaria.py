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
            """ print(str(bin_n) + ' es n y ' + str(bin_m) + ' es m')
            print('distancia es igual a ' + str(distance)) """
        i += 1
    return distance

print(distancia_binaria(12,32))


def son_aledaños(n:int, m:int) -> bool:
    '''
    completar docstring
    '''


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

""" def entero_a_binario(n:int) -> str:
    '''
    Requiere: n > 0.
    Devuelve: n convertido a binario.
    '''
    r:int = 0
    c:int = 0
    res:str = '' 
    invert:str = ''
    while n > 0:
        r = n%2
        c = n//2
        n= 2 * c + r
        res = res + str(r)
        n = c
        print(n)
    count:int = len(res) - 1
    while count >= 0:
        invert = invert + (res[count])
        count = count - 1
    res = invert
    return res """

