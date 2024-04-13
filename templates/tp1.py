from distancia_binaria import distancia_binaria, son_aledaños, \
                   aledaños_menores, cant_aledaños, densidad_intervalo

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario según la siguiente codificación:
        A -> Distancia binaria;
        B -> Son vecinos binarios aledaños;
        C -> Lista vecinos binarios aledaños menores;
        D -> Cantidad de aledaños en intervalo;
        E -> Densidad binaria;
        F -> Finalizar;
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás.
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Distancia binaria [n,m]')
    print('B. Son vecinos binarios aledaños [n,m]')
    print('C. Lista vecinos binarios aledaños menores [n]')
    print('D. Cantidad de aledaños en intervalo [n,a,b]')
    print('E. Densidad binaria [n,a,b]')
    print('F. Finalizar')
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida


# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        n_str:str = input('Ingrese n: ')
        # [COMPLETAR]

    elif opcion_seleccionada == 'B':
        n_str:str = input('Ingrese n: ')
        # [COMPLETAR]

    elif opcion_seleccionada == 'C':
        # [COMPLETAR]

    elif opcion_seleccionada == 'D':
        # [COMPLETAR]

    elif opcion_seleccionada == 'E':
        # [COMPLETAR]

    elif opcion_seleccionada == 'F':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        input('Presione ENTER para continuar.')
