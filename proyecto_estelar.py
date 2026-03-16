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

    def __init__(self, IdCombate: str, Clave: int):
        self.IdCombate = IdCombate
        self.__Clave = Clave

class Nave(UnidadesCombateEstelares):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list):
        super().__init__(IdCombate, Clave)
        self.Nombre = Nombre
        self.PiezasRepuesto = PiezasRepuesto

class EstacionEstelar(Nave):
    
    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list,  Tripulacion: int, Pasaje: int, Ubicacion: EUbicacion): 
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Tripulacion = Tripulacion
        self.Pasaje = Pasaje
        self.Ubicacion = Ubicacion

class NaveEstelar(Nave):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list, Tripulacion: int, Pasaje: int, Clase: EClase):
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Tripulacion = Tripulacion
        self.Pasaje = Pasaje
        self.clase = Clase

class CazaEstelar(Nave):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list, Dotacion: int):
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Dotacion = Dotacion
