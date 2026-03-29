from proyecto_estelar import *
import pytest

'''Aqui vamos a crear un conjunto de test para comprobar la funcionalidad de nuestro programa.'''

'''TEST 1. Para comprobar que el operario añade piezas correctamente'''
def test_añadir_repuesto():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)
    motor = Repuesto('Motor Ionico', 'Sienar', 10, 2400)

    operario.añadir_repuesto(motor)

    assert len(almacen.catalogo_repuestos) == 1
    assert almacen.catalogo_repuestos[0].get_nombre() == 'Motor Ionico'


'''TEST 2. Comprobar que se actualiza el stock si el repuesto existe.'''
def test_operario_añadir_repuesto_existente():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)

    motor1 = Repuesto('Motor Ionico', 'Sienar', 10, 2400)
    operario.añadir_repuesto(motor1)

    motor2 = Repuesto('Motor Ionico', 'Sienar', 5, 2400)
    operario.añadir_repuesto(motor2)

    assert len(almacen.catalogo_repuestos) == 1
    assert almacen.catalogo_repuestos[0].get_cantidad_disponible() == 15


'''TEST 3. Comprobar que se actualiza el stock cuando eliminamos un repuesto.'''
def test_operario_eliminar_repuesto():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)
    motor = Repuesto('Motor Ionico', 'Sienar', 10, 2400)

    operario.añadir_repuesto(motor)
    assert len(almacen.catalogo_repuestos) == 1

    resultado = operario.eliminar_repuesto('Motor Ionico', 'Sienar')

    assert resultado == True
    assert len(almacen.catalogo_repuestos) == 0


'''TEST 4. Comprobar que salta la excepción cuando se intenta eliminar un repuesto no existente'''
def test_operario_eliminar_repuesto_inexistente():
    almacen = Almacen('Almacen Estelar 1', 'Tatooine')
    operario = Operario('Operario 1', 1234, almacen)

    with pytest.raises(ErrorRepuestoNoEncontrado):
        operario.eliminar_repuesto('Motor Inexistente', 'Sienar')


'''TEST 5. Comprobación método adquirir repuesto, comprobamos que funcione correctamente el proceso de selección de piezas eligiendo siempre a más barata.'''
def test_comandante_adquirir_repuesto():
    caza = CazaEstelar(id_combate="TIE-01", clave=123, nombre="TIE Fighter", piezas_repuesto=[], dotacion=1)
    vader = Comandante("Vader", 0000, caza)

    almacen_barato = Almacen('Almacen Borde Exterior', 'Tatooine')
    almacen_caro = Almacen('Almacen Nucleo', 'Coruscant')
    
    motor_barato = Repuesto('Motor Ionico', 'Sienar', 2, 1000)
    almacen_barato.catalogo_repuestos.append(motor_barato)
    
    motor_caro = Repuesto('Motor Ionico', 'Kuat', 5, 5000)
    almacen_caro.catalogo_repuestos.append(motor_caro)
    
    almacenes_del_imperio = [almacen_caro, almacen_barato] 
    
    resultado = vader.adquirir_repuesto('Motor Ionico', almacenes_del_imperio, 3)
    
    assert resultado == True 
    
    assert len(vader.nave_asignada.piezas_repuesto) == 3 
    
    assert motor_barato.get_cantidad_disponible() == 0 

    assert motor_caro.get_cantidad_disponible() == 4