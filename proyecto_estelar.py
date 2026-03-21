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

    def get_clave(self):
        return self.__clave

class Nave(UnidadesCombateEstelares):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list):
        super().__init__(id_combate, clave)
        self.nombre = nombre
        self.piezas_repuesto = []

class EstacionEspacial(Nave):
    
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

    def get_precio(self): # método get para precio definido
        return self.precio
    
    def get_cantidad_disponible(self): # método get para cantidad definido
        return self.__cantidad_disponible

    def set_cantidad_disponible(self, cantidad_disponible): # metodo set para cantidad definido
        self.__cantidad_disponible = cantidad_disponible

class Almacen:
    def __init__(self, nombre : str, localizacion: str):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo_repuesto = []
        
class UsuarioSistema:
    def __init__(self, id_usuario : str, clave_usuario : int):
        self.id_usuario = id_usuario
        self.__clave_usuario = clave_usuario
        
class Comandante(UsuarioSistema):
    ''' 
    En nuestro gestor de mantenimiento de la flota, el Comandante será el encargado de gestionar su nave, por tanto él será el único 
    que conozca las piezas que necesita así pues, sugre la necesidad de poder conocer el precio, stock disponible de un repuesto 
    concreto, así como la posibilidad de comprar dicho repuesto. El Comandante a la hora de adqurir una pieza, no se preocupa del 
    almacen en el que se encuentra la pieza, simplemente si la pieza está o no, sin importar donde se encuentre.
    
    Así por tanto, una vez tenga la pieza adquirida esta se adjuntará a su propia nave, puede que se instale o simplemente este a modo de reserva.
    '''
    def __init__(self, id_usuario : str, clave_usuario : int, nave_asignada : str):

        super().__init__(id_usuario, clave_usuario)
        
        self.nave_asignada = nave_asignada
    
    def consultar_disponibilidad(self, nombre_pieza : str, almacenes_imperio : list): 
        ''' Buscamos la pieza entre los distintos catálogos de cada uno de los almacenes del Imperio Galáctico y devolvemos si la pieza se encuentra disponible.'''
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and repuesto.get_cantidad_disponible() > 0:
                    return True
    
    def consultrar_precio(self, nombre_pieza : str, almacenes_imperio : list , precio : float):
        ''' Para una pieza concreta, buscamos el precio que tiene'''  
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and repuesto.get_cantidad_disponible() > 0:
                    return repuesto.get_precio() # definir método get
                
    def adquirir_repuesto(self, nombre_pieza : str, almacenes_imperio : list , cantidad : int ):
        '''Buscamos la pieza y la cantidad desdeada'''
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and (repuesto.get_cantidad_disponible() - cantidad) > 0:
                    
                    nuevo_stock = repuesto.get_cantidad_disponible() - cantidad
                    repuesto.set_cantidad(nuevo_stock) # definir método set
                    self.nave_asignada.piezas_repuesto.append(nombre_pieza) # añadimos el repuesto a la nave del comandante.
                    return True
        return False
                    
class Operario(UsuarioSistema):
    '''
    En nuestro software gestor contratado por el Imperio Galáctico, la función de los operarios será el mantenimiento de los 
    almacenes que se encuentran por la galaxia. Un operario esta ligado a un almacen, su objetivo será dada una entrada de repuestos
    que le lleguen 'ordenarlos' en el catálogo del almacen. No obstate, también se pueden dar otras situaciones como que llegue un 
    nuevo modelo de un repuesto y el operario decida descatalogar el modelo antiguo. 
    '''
    
    def __init__(self, id_usuario : str, clave_usuario : int, almacen_asignado : str):
        super().__init__(id_usuario, clave_usuario)
        
        self.almacen_asignado = almacen_asignado
        
    def añadir_repuesto(self, nombre_repuesto : str) :
        ''' Añadimos un nuevo repuesto'''
        self.almacen_asignado.catalogo_repuestos.append(nombre_repuesto)
        
    def eliminar_repuesto(self, nombre_repuesto : str):
        '''Eliminamos repuesto'''
        self.almacen_asignado.catalogo_repuestos.remove(nombre_repuesto)
        
    def modificar_stock(self, nombre_repuesto : str, nueva_cantidad : int):
        '''Dado un repuesto modificamos el stock'''
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if repuesto == nombre_repuesto:
                repuesto.set_cantidad_disponible(nueva_cantidad) # definir metodo set
        


if __name__ == '__main__':
# definimos clases
    unidad_aerea = UnidadesCombateEstelares(id_combate=1, clave=0)
    caza = Nave(nombre='Caza Moderno', piezas_repuesto=['piston', 'bomba de combustible', 'faros estelares'])
    
