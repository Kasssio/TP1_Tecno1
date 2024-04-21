def distancia_binaria(n:int, m:int) -> int:
    '''
    Requiere: n > 0 y m > 0.
    Devuelve: La distancia binaria entre n y m.
    '''
    i:int = 0
    distance:int = 0
    bin_n:str = bin(n).replace('0b','')
    bin_m:str = bin(m).replace('0b','')

    if len(bin_n) < len(bin_m): # Este condicional existe para igualar la longitud de n y m, así sacamos la verdadera distancia.
        bin_n = ('0' * (len(bin_m) - len(bin_n))) + bin_n
    elif len(bin_m) < len(bin_n):
        bin_m = ('0' * (len(bin_n) - len(bin_m))) + bin_m

    while i < len(bin_n):
        if bin_n[i] != bin_m[i]:
            distance += 1
        i += 1
    return distance

def son_aledaños(n:int, m:int) -> bool:
    '''
    Requiere: n y m > 0.
    Devuelve: un bool que determina si la distancia entre los dos es 1 o no.
    '''
    isVecinos:bool = False
    distance:int = distancia_binaria(n,m)

    if distance != 1 or distance == 0: isVecinos = False
    else: isVecinos = True
    return isVecinos

def aledaños_menores(n:int) -> list[int]:
    '''
    Requiere: n > 0.
    Devuelve: una lista de los vecinos binarios aledaños de n.
    '''
    i:int = 1
    total:list[int] = []
    while i < n:
        temp:bool = son_aledaños(n,i)
        if(temp == True):
            total.append(i)
        i += 1
    return total
    # creamos un while que por cada intervalo, mientras i sea menor a n, use la funcion son_aledaños() entre n e i para confirmar que sean vecinos. 
    # si se cumple esto, appendear el valor de i en ese intervalo a la lista. 

def cant_aledaños(n:int, a:int, b:int) -> int:
    '''
    Requiere: n,a,b > 0.
    Devuelve: La cantidad de vecinos aledaños entre n y los números en el intervalo [a,b].
    '''

    i:int = a
    cant:int = 0
    while i <= b:
        check:bool = son_aledaños(i,n)
        if check:
            cant += 1
        i += 1
    return cant

def densidad_intervalo(n:int, a:int, b:int) -> float:
    '''
    Requiere: n,a,b > 0.
    Devuelve: El cociente entre la cantidad de vecinos aledaños a n en [a,b] y la cantidad de enteros en [a,b]
    '''
    vecinos:int = cant_aledaños(n,a,b)
    enteros:int = b - a + 1 
    res:float = vecinos / enteros
    res = round(res,5)
    return res

print(densidad_intervalo(64,1,63))