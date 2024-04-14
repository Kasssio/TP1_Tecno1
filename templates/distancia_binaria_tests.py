import unittest

# Se importa el código a testear.
from distancia_binaria import distancia_binaria, son_aledaños, \
                   aledaños_menores, cant_aledaños, densidad_intervalo

#####################################################################

class TestVecinosBinarios(unittest.TestCase):
    ## ATENCION: los nombres de estas funciones deben empezar con test_

    def test_distancia_binaria(self):
        ...

    def test_son_aledaños(self):
        ...

## y asi con el resto de las funciones a testear.

unittest.main()
