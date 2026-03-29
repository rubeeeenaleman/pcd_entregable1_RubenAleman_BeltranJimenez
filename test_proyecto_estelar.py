from proyecto_estelar import *
import pytest

'''Aqui vamos a crear un conjunto de test para comprobar la funcionalidad de nuestro programa.'''

'''TEST 1. Para comprobar que el operario añade piezas correctamente'''
def test_añadir_repuesto():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)
    motor = Repuesto('Motor Ionico', 'Sienar', 10, 2400)

    operario.añadir_repuesto(motor)

    '''comprobacion'''
    assert len(almacen.catalogo_repuestos) == 1
    assert almacen.catalogo_repuestos[0].get_nombre() == 'Motor Ionico'


'''TEST2 2. Comprobar que se actualiza el stock si el repuesto existe.'''
def test_operario_añadir_repuesto_existente():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)

    motor1 = Repuesto('Motor Ionico', 'Sienar', 10, 2400)
    operario.añadir_repuesto(motor1)

    motor2 = Repuesto('Motor Ionico', 'Sienar', 5, 2400)
    operario.añadir_repuesto(motor2)

    assert len(almacen.catalogo_repuestos) == 1
    assert almacen.catalogo_repuestos[0].get_cantidad_disponible() == 15