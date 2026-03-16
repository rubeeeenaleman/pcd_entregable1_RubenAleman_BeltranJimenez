class UnidadesCombateEstelares:

    def __init__(self, IdCombate: str, Clave: int):
        self.IdCombate = IdCombate
        self.__Clave = Clave

class Nave(UnidadesCombateEstelares):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list):
        super().__init__(IdCombate, Clave)
        self.Nombre = Nombre
        self.PiezasRepuesto = PiezasRepuesto

class EstacionEstelar(UnidadesCombateEstelares, Nave):
    
    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list,  Tripulacion: int, Pasaje: int): # faltan las enumeraciones.
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Tripulacion = Tripulacion
        self.Pasaje = Pasaje

class NaveEstelar(UnidadesCombateEstelares, Nave):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list, Tripulacion: int, Pasaje: int):
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Tripulacion = Tripulacion
        self.Pasaje = Pasaje

class CazaEstelar(UnidadesCombateEstelares, Nave):

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list, Dotacion: int):
        super().__init__(IdCombate, Clave, Nombre, PiezasRepuesto)
        self.Dotacion = Dotacion