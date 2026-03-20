from enum import Enum

class EUbicacion(Enum):
    ENDOR = 1
    CUMULO_RAIMOS = 2
    NEBULOSA_KALIIDA = 3

class EClase(Enum):
    EJECUTOR = 1
    ECLIPSE = 2
    SOBERANO = 3


class UnidadesCombateEstelares:

    def __init__(self, id_combate: str, clave: int):
        self.id_combate = id_combate
        self.__clave = clave

class Nave(UnidadesCombateEstelares):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list):
        super().__init__(id_combate, clave)
        self.nombre = nombre
        self.piezas_repuesto = piezas_repuesto

class EstacionEstelar(Nave):
    
    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, tripulacion: int, pasaje: int, ubicacion: EUbicacion): 
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

class NaveEstelar(Nave):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, tripulacion: int, pasaje: int, clase: EClase):
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase

class CazaEstelar(Nave):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, dotacion: int):
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.dotacion = dotacion

class Repuesto:
    def __init__(self, nombre_repuesto : str, provedor : str,  cantidad_disponible : int, precio : float):
        self.nombre_repuesto = nombre_repuesto
        self.provedor = provedor
        self.__cantidad_disponible = cantidad_disponible
        self.precio = precio

class Almacen:
    def __init__(self, nombre : str, localizacion: str):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo_repuesto = []
        
class UsuarioSistema:
    def __init__(self, id_usuario : str, clave_usuario : int):
        self.id_usuario = id_usuario
        self.__clave_usuario = clave_usuario