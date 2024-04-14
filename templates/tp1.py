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
        m_str:str = input('Ingrese m: ')

        n_int:int = int(n_str)
        m_int:int = int(m_str)

        func = str(distancia_binaria(n_int,m_int))

        print('La distancia binaria entre ' + n_str + ' y ' + m_str + ' es ' + func)
    elif opcion_seleccionada == 'B':
        n_str:str = input('Ingrese n: ')
        m_str:str = input('Ingrese m: ')

        n_int:int = int(n_str)
        m_int:int = int(m_str)

        func = son_aledaños(n_int,m_int)

        if(func == True): 
            print('Los números ' + n_str + ' y ' + m_str + ' son vecinos binarios aledaños')
        else: 
            print('Los números ' + n_str + ' y ' + m_str + ' no son vecinos binarios aledaños')


        

    elif opcion_seleccionada == 'C':
        n_str:str = input('Ingrese n: ')
        n_int:int = int(n_str)
        func = aledaños_menores(n_int)
        if func != []:
            print('Los números ' + str(func) + ' son vecinos aledaños de ' + n_str + ' menores a ' + n_str)
        else:
            print('El número ' + n_str + ' no tiene vecinos aledaños menores')

    elif opcion_seleccionada == 'D':
        # [COMPLETAR]
        pass #para que no tire error cuando esté vacío

    elif opcion_seleccionada == 'E':
        # [COMPLETAR]
        pass #para que no tire error cuando esté vacío

    elif opcion_seleccionada == 'F':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        input('Presione ENTER para continuar.')

