class UnidadesCombateEstelares:

    def __init__(self, IdCombate: str, Clave: int):
        self.IdCombate = IdCombate
        self.__Clave = Clave

class Nave:

    def __init__(self, IdCombate: str, Clave: int, Nombre: str, PiezasRepuesto: list):
        super().__init__(IdCombate, Clave)
        self.Nombre = Nombre
        self.PiezasRepuesto = PiezasRepuesto