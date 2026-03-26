from enum import Enum
from abc import ABC, abstractmethod

class EUbicacion(Enum):
    ENDOR = 1
    CUMULO_RAIMOS = 2
    NEBULOSA_KALIIDA = 3

class EClase(Enum):
    EJECUTOR = 1
    ECLIPSE = 2
    SOBERANO = 3


class UnidadesCombateEstelares(ABC):
    '''    
    Implementamos como clase abstracta, pues la unidad de 
    combate no es una 
    nave o vehículo concreto, sino un concepto general que 
    representa un elemento de la flota.
    '''
    
    def __init__(self, id_combate: str, clave: int):
        self.id_combate = id_combate
        self.__clave = clave

    def get_clave(self):
        return self.__clave
    
    @abstractmethod 
    def mostrar_especificaciones(self):
        pass # no devuelve nada, simplemente obliga a que las clases nietos tengan esta función.

class Nave(UnidadesCombateEstelares):
    '''
    Decidimos no ponerme el método asbtracto, pues relamente
    este objeto Nave, no represetna una nave concreta, sino un 
    concepto de las características básicas que debe de tener 
    una nave.
    Así pues, debido a la herencia, está tambíen será una clase asbtracta
    '''
    
    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list):
        super().__init__(id_combate, clave)
        self.nombre = nombre
        self.piezas_repuesto = piezas_repuesto

class EstacionEspacial(Nave):
    
    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, tripulacion: int, pasaje: int, ubicacion: EUbicacion): 
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.ubicacion = ubicacion

    def mostrar_especificaciones(self):
        return f"Estación {self.nombre}, operando en {self.ubicacion.name}.A bordo {self.tripulacion} tripulantes y con capacidad para {self.pasaje} pasajeros."


class NaveEstelar(Nave):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, tripulacion: int, pasaje: int, clase: EClase):
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.tripulacion = tripulacion
        self.pasaje = pasaje
        self.clase = clase
        
    def mostrar_especificaciones(self):
        return f"Nave estelar {self.nombre}, clase {self.clase.name}.A bordo {self.tripulacion} tripulantes y con capacidad para {self.pasaje} pasajeros."
    
class CazaEstelar(Nave):

    def __init__(self, id_combate: str, clave: int, nombre: str, piezas_repuesto: list, dotacion: int):
        super().__init__(id_combate, clave, nombre, piezas_repuesto)
        self.dotacion = dotacion

    
    def mostrar_especificaciones(self):
        return f"Caza {self.nombre}, con ID de comabte: {self.id_combate} . "
    
    
class Repuesto:
    def __init__(self, nombre_repuesto : str, proveedor : str,  cantidad_disponible : int, precio : float):
        self.nombre_repuesto = nombre_repuesto
        self.proveedor = proveedor
        self.__cantidad_disponible = cantidad_disponible
        self.precio = precio

    def get_nombre(self):
        return self.nombre_repuesto
    
    def get_precio(self): 
        return self.precio
    
    def get_cantidad_disponible(self): 
        return self.__cantidad_disponible
    
    def get_proveedor(self):
        return self.proveedor

    def set_cantidad_disponible(self, nueva_cantidad): 
        self.__cantidad_disponible = nueva_cantidad
    
    def __lt__(self, otro_repuesto): # método less than para poder comparar repuestos por precio
        return self.get_precio() < otro_repuesto.get_precio()
        
        
class Almacen:
    def __init__(self, nombre : str, localizacion: str):
        self.nombre = nombre
        self.localizacion = localizacion
        self.catalogo_repuestos = []
        
class UsuarioSistema(ABC):
    '''
    UsuariosSistema será una clase abstracta, porque no representa un entre concreto.
    Su funcionalidad es de clase base para determinar los atributos mínimos necesarios para poder estar en el sistema.
    '''
    
    def __init__(self, id_usuario : str, clave_usuario : int):
        self.id_usuario = id_usuario
        self.__clave_usuario = clave_usuario
    
    @abstractmethod 
    def mostrar_informacion(self):
        pass # no devuelve nada, simplemente obliga a que las clases hijas tengan esta función.
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
    
    
    def mostrar_informacion(self):
        return f"Comandante {self.id_usuario} encargado de {self.nave_asignada.nombre}"

    
    def consultar_disponibilidad(self, nombre_pieza : str, almacenes_imperio : list): 
        ''' Buscamos la pieza entre los distintos catálogos de cada uno de los almacenes del Imperio Galáctico y devolvemos si la pieza se encuentra disponible.'''
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuestos:
                if repuesto.get_nombre() == nombre_pieza and repuesto.get_cantidad_disponible() > 0:
                    return True
    
    def consultar_precio(self, nombre_pieza : str, almacenes_imperio : list ):
        ''' Para una pieza concreta, buscamos el precio que tiene y además, se devuelve la pieza con menor precio entre todas ellas.'''  
        precio_mas_bajo = float('inf')
        pieza_encontrada = False
        repuesto_mas_barato = None

        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuestos:
                if repuesto.get_nombre() == nombre_pieza and repuesto.get_cantidad_disponible() > 0:
                    pieza_encontrada = True
                    if repuesto.get_precio() < precio_mas_bajo:
                        precio_mas_bajo = repuesto.get_precio()
                        repuesto_mas_barato = repuesto.get_nombre()
        
        if pieza_encontrada:
            return f"Mejor precio {precio_mas_bajo}, para el repuesto {repuesto_mas_barato}"
        else:
            return None
                
    def adquirir_repuesto(self, nombre_pieza : str, almacenes_imperio : list , cantidad : int ):
        '''Adquiere el número de repuestos necesarios en ese momento para una nave, actualiza el stock y además hace una consulta eficiente, quedándose con los repuestos más baratos.'''
        repuestos_mas_baratos = []
        stock_total = 0

        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuestos:
                if repuesto.get_nombre() == nombre_pieza and (repuesto.get_cantidad_disponible()) > 0:
                    repuestos_mas_baratos.append(repuesto)
                    stock_total += repuesto.get_cantidad_disponible()
        
        # esta parte podría ser tratada como una excepción más adelante
        if stock_total < cantidad:
            print('Error: No hay suficiente stock en la galaxia.')
            return False
        
        repuestos_mas_baratos.sort() # ordenamos los repuestos que hemos insertado en la lista por precio de menor a mayor (funciona gracias al método lt)
        # recorremos la lista ordenada por precio en orden ascendente
        for repuesto in repuestos_mas_baratos: 
            while cantidad > 0 and repuesto.get_cantidad_disponible() > 0:
                nuevo_stock = repuesto.get_cantidad_disponible() - 1 #  recordamos que ahora la selección se hace de uno en uno
                repuesto.set_cantidad_disponible(nuevo_stock)

                self.nave_asignada.piezas_repuesto.append(nombre_pieza)
                cantidad = cantidad - 1
        return True
                    
class Operario(UsuarioSistema):
    '''
    En nuestro software gestor contratado por el Imperio Galáctico, la función de los operarios será el mantenimiento de los 
    almacenes que se encuentran por la galaxia. Un operario esta ligado a un almacen y su objetivo será dada una entrada de repuestos 
    que le lleguen 'ordenarlos' en el catálogo del almacen. No obstante, también se pueden dar otras situaciones como que llegue un 
    nuevo modelo de un repuesto y el operario decida descatalogar el modelo antiguo. O una entrada masiva de un repuesto muy popular y tener que hacer 
    una modificación grande del stock.
    
    Tambíen, los operarios están muy concienciados con los tiempos de espera (que en el sistema gestor no se aprecian), así por tanto, si un repuesto es muy popular en las cercanias de un almacén concreto, los operadores que trabajan allík, querrán tener el máximo stock posible del repuesto, para poder entregarlos de manera dinámica. Cuando el proveedor no puede absatecer dicha demanda y en almacenes lejanos el porducto no es tan popular, lo mejor para la correcta gestión del Imperio Galácitco, sera poder abastecer el almacén popular.
    Por tanto surge la encesidad, de poder transferir repuestos entre almacenes.
    
    El operario a la hora de identificar un Repuesto, no puede hacerlo unícamente por el nombre, pues el mismo repuesto puede venir de diferentes proveedores y con distitno precio.
    Por tanto, hemos decidido que lo mejor sera identificar un repuesto concreto por la tupla: nombre, proveedor. Esta consideración, no es tomada para comandnate, ya que ellos
    no están tan relacionados con lso técnicimos que puede dar un repuesto según el proveedor.
    '''
    
    def __init__(self, id_usuario : str, clave_usuario : int, almacen_asignado : str):
        super().__init__(id_usuario, clave_usuario)
        
        self.almacen_asignado = almacen_asignado
    
    def mostrar_informacion(self):
        return f"Operario {self.id_usuario}, trabajdor del almacen: {self.almacen_asignado.nombre}"

            
    def añadir_repuesto(self, nuevo_repuesto : Repuesto) :
        ''' Se trata de añadir un neuvo repuesto, en el caso de que exista, se incremetna su stock.'''
        nombre_repuesto= nuevo_repuesto.get_nombre()
        proveedor= nuevo_repuesto.get_proveedor()
        
        for pieza in self.almacen_asignado.catalogo_repuestos:
            if nombre_repuesto == pieza.get_nombre() and proveedor == pieza.get_proveedor():
                nuevo_stock = pieza.get_cantidad_disponible() + 1 
                pieza.set_cantidad_disponible(nuevo_stock)
                return True
        self.almacen_asignado.catalogo_repuestos.append(nuevo_repuesto)
        
    def eliminar_repuesto(self, nombre_repuesto : str, proveedor  : str):
        '''Eliminamos repuesto'''
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if nombre_repuesto == repuesto.get_nombre() and proveedor == repuesto.get_proveedor():
                self.almacen_asignado.catalogo_repuestos.remove(repuesto)
                return True # la operación ha sido realizada con éxito
        return "ERROR" # añadimos excepción

        
    def modificar_stock(self, nombre_repuesto : str, proveedor  : str, nueva_cantidad : int):
        '''Dado un repuesto modificamos el stock, para no tener que ir incremetnado o decrementando de 1 en 1.'''
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if nombre_repuesto == repuesto.get_nombre() and proveedor == repuesto.get_proveedor():
                repuesto.set_cantidad_disponible(nueva_cantidad) 
        return 'ERROR'
    
    
    def transferir_repuesto(self, almacen_destino, nombre_repuesto: str, proveedor  : str) :
        """Mueve un repuesto entero desde el almacén actual a otro almacén del Imperio."""
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if nombre_repuesto == repuesto.get_nombre() and proveedor == repuesto.get_proveedor():
                # Añadimos al almacén destino y eliminamos del actual
                almacen_destino.catalogo_repuestos.append(repuesto)
                self.almacen_asignado.catalogo_repuestos.remove(repuesto)
                return True
        return 'ERROR'
if __name__ == '__main__':
    # EJEMPLO DE PRUEBA PARA EL FUNCIONAMIENTO DE LA MAYORÍA DE FUNCIONES DEFINIDAS
    
    # BLOQUE DE LAS NAVES
    unidad_aerea = UnidadesCombateEstelares(id_combate="U-001", clave=1234)
    caza = Nave(id_combate="N-002", clave=5555, nombre='Caza Moderno',piezas_repuesto=['piston', 'bomba'])
    estacion = EstacionEspacial(id_combate="E-003", clave=9999, nombre="Estrella de la Muerte", piezas_repuesto=["Láser"], tripulacion=50, pasaje=4, ubicacion=EUbicacion.ENDOR)

    print(f'Prueba unidad aerea: \n id de combate: {unidad_aerea.id_combate}, clave: {unidad_aerea.get_clave()}') # hay que recordar que clave es un atributo privado, sin ayuda del metodo get, obtendriamos error 
    
    # BLOQUE DE ALMACEN Y DERIVADS
    almacen_tatooine = Almacen(nombre="Base Logística Tatooine", localizacion="Borde Exterior")
    operario = Operario(id_usuario="OP-421", clave_usuario=3333, almacen_asignado=almacen_tatooine)
    
    # REPUESTO
    motor = Repuesto(nombre_repuesto="Motor Iónico", proveedor="Sienar", cantidad_disponible=5, precio=2500.0)
    
    print(f"\nOperario {operario.id_usuario} trabajando en el alamcen :  {almacen_tatooine.nombre}")
    
    # Veamos algunas de sus funciones
    operario.añadir_repuesto(motor)
    print(f"Se ha añadido '{motor.get_nombre()}' al catálogo.")
    print(f"Stock inicial: {motor.get_cantidad_disponible()} unidades.")
    
    
    operario.modificar_stock(nombre_repuesto="Motor Iónico", nueva_cantidad=50)
    print(f"Stock tras la actualización del operario: {motor.get_cantidad_disponible()} unidades.")

    #Porbemos la clase Comandante
    vader = Comandante(id_usuario="Darth Vader", clave_usuario=0000, nave_asignada=caza)
    print(f"\nComandante {vader.id_usuario} concetado al software del Imperio Galáctico. Nave asignada: {vader.nave_asignada.nombre}.")
    
    
