import unittest

# Se importa el código a testear.
from distancia_binaria import distancia_binaria, son_aledaños, \
                   aledaños_menores, cant_aledaños, densidad_intervalo

#####################################################################

class TestVecinosBinarios(unittest.TestCase):  
    def test_distancia_binaria(self):
        self.assertEqual(distancia_binaria(6,18),2)
        self.assertEqual(distancia_binaria(1,100),4)
        self.assertEqual(distancia_binaria(12,12),0)
        self.assertEqual(distancia_binaria(50,50),0)
        self.assertEqual(distancia_binaria(14,3),3)
        self.assertEqual(distancia_binaria(100,1),4)

    def test_son_aledaños(self):
        self.assertEqual(son_aledaños(14,3),False)
        self.assertEqual(son_aledaños(1,100),False)
        self.assertEqual(son_aledaños(3,3),False)
        self.assertEqual(son_aledaños(50,51),True)
        self.assertEqual(son_aledaños(3,2),True)
        self.assertEqual(son_aledaños(5,4),True)

    def test_aledaños_menores(self):
        self.assertEqual(aledaños_menores(127),[63, 95, 111, 119, 123, 125, 126])
        self.assertEqual(aledaños_menores(64),[])
        self.assertEqual(aledaños_menores(5),[1, 4])
        self.assertEqual(aledaños_menores(1),[])
        self.assertEqual(aledaños_menores(10),[2, 8])
        self.assertEqual(aledaños_menores(100),[36, 68, 96])

    def test_cant_aledaños(self):
        self.assertEqual(cant_aledaños(10,8,13),2)
        self.assertEqual(cant_aledaños(64,1,63),0)
        self.assertEqual(cant_aledaños(10,1,100),7)
        self.assertEqual(cant_aledaños(10,100,1),0)

    def test_densidad_intervalo(self):
        self.assertEqual(densidad_intervalo(10,8,13),0.33333)
        self.assertEqual(densidad_intervalo(64,1,63),0.0)
        self.assertEqual(densidad_intervalo(100,50,100),0.03922)
        self.assertEqual(densidad_intervalo(50,20,80),0.09804)
 
unittest.main()
