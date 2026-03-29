'''
MEJORAS A REALIZAR:
'''

class Comandante(UsuarioSistema):
    ''' 
    En nuestro gestor de mantenimiento de la flota, el Comandante será el encargado de gestionar su nave, por tanto él será el único que conozca las piezas que necesita así pues, sugre la necesidad de poder conocer el precio, stock disponible de un repuesto concreto, así como la posibilidad de comprar dicho repuesto. El Comandante a la hora de adqurir una pieza, no se preocupa del almacen en el que se encuentra la pieza, simplemente si la pieza está o no, sin importar el alamcen en donde se encuentre.
    
    Así por tanto, una vez tenga la pieza adquirida esta se adjuntará a su propia nave, puede que se instale o simplemente este a modo de reserva.
    '''
    def __init__(self, id_usuario : str, clave_usuario : int, nave_asignada : str):

        super().__init__(id_usuario, clave_usuario)
        
        self.nave_asignada = nave_asignada
    
    def consultar_disponibilidad(self, nombre_pieza : str, almacenes_imperio : list): 
        ''' Buscamos la pieza entre los distintos catálogos de cada uno de los almacenes del Imperio Galáctico y devolvemos si la pieza se encuentra disponible.'''
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and repuesto.get_canitdad() > 0:
                    return True
    
    def consultrar_precio(self, nombre_pieza : str, almacenes_imperio : list , precio : float):
        ''' Para una pieza concreta, buscamos el precio que tiene'''  
        # MEJORA, DEVOVLER LA PIEZA CON EL MENOR PRECIO DE ENTRE TODAS, PUES SEGUN EL ALMACEN, TAL VEZ TENGA UN PRECIO MAYOR O MENOR
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and repuesto.get_canitdad() > 0:
                    return repuesto.get_precio()
                
    def adquirir_repuesto(self, nombre_pieza : str, almacenes_imperio : list , cantidad : int ):
        # MEJORAS:
        # QUE NO UNICAMENTE SE CENTRE EN UN ALMACEN, SINO QUE BUSQUE LA PIEZA MÁS BARTA SI SOLO HAY 1, QUE COJA ESA Y LUEGO LA SIGUIENTE MÁS BARATA Y ASÍ HASTA RELLENAR SU PETICIÓN, NO QUE BUSQUE UN ALMACEN QUE TENGA EL NUMERO DE PIEZAS QUE QUIERE
        '''Buscamos la pieza y la cantidad desdeada'''
        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuesto:
                if repuesto == nombre_pieza and (repuesto.get_canitdad() - cantidad) > 0:
                    
                    nuevo_stock = repuesto.get_cantidad() - cantidad
                    repuesto.set_cantidad(nuevo_stock)
                    self.nave_asignada.piezas_repuesto.append(nombre_pieza)
                    return True
        return False
    
    
    
class Operario(UsuarioSistema):
    '''
    En nuestro software gestor contratado por el Imperio Galáctico, la función de los operarios será el mantenimiento de los 
    almacenes que se encuentran por la galaxia. Un operario esta ligado a un almacen, su objetivo será dada una entrada de repuestos
    que le lleguen 'ordenarlos' en el catálogo del almacen. No obstate, también se pueden dar otras situaciones como que llegue un 
    nuevo modelo de un repuesto y el operario decida descatalogar el modelo antiguo.
    
    
    
    AÑADIR ALGO COMO
    Tambíen, se puede dar la situación de que los operadores esten concienciados con los tiempos de envio, si en las cercanias de un almacne concreto suelen pedir mucho de un repuesto, los operadores pueden llegar a un acuerdo de intercambiarse piezas desde un almacen a otro . DEBEMOS CREAR UAN FUNCIÓN TIPO transferir_pieza() 
    '''
    
    def __init__(self, id_usuario : str, clave_usuario : int, almacen_asignado : str):
        super().__init__(id_usuario, clave_usuario)
        
        self.almacen_asignado = almacen_asignado
     
    # OTRA ANOTACIÓN MÁS, DEBEMOS DE PLANTEARNOS QUE 1 MISMA PIEZA PERO CON DISTINTO PRECIO O DISTINTO PROVEDOR SON DOS OBJETOS DIFERENTES, ENTONCES AL AÑADIR O ELIMINAR SOBRE CUAL LO HACEMOS, ¿CREAMOS UN NUEVO OBJETO? O ENTRAMOS EN EL DETALLE de que cada piesza tiene un precio o provedor distitno.
    
         
    def añadir_repuesto(self, nombre_repuesto : str):
        ''' Añadimos un nuevo repuesto'''
        # DEBEMOS DE HACER UNA COMRBOACÍN DE QUE EL REPUESTO EXISTA Y SI EXISTE SUMAR EN 1 AL STOCK DEL REPUESTO
        self.almacen_asignado.catalogo_repuestos.append(nombre_repuesto)
        
    def eliminar_repuesto(self, nombre_repuesto : str):
        '''Eliminamos repuesto'''
        # DEBEMOS DE COMPROBAR QUE SE PUEDA ELIMINAR
        self.almacen_asignado.catalogo_repuestos.remove(nombre_repuesto)
        
    def modificar_stock(self, nombre_repuesto : str, nueva_cantidad : int):
        # COMPROBACIÓN DE QUE EXISTA
        '''Dado un repuesto modificamos el stock'''
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if repuesto == nombre_repuesto:
                repuesto.set_cantidad(nueva_cantidad)
                
                
    # POSIBLE FUNCIÓN_transferir pieza:
    def transferir_repuesto(self, almacen_destino, nombre_pieza: str) -> bool:
        """Mueve un repuesto entero desde el almacén actual a otro almacén del Imperio."""
        # Buscamos la pieza en nuestro almacén
        for repuesto in self.almacen_asignado.catalogo_repuestos:
            if repuesto.nombre_repuesto == nombre_pieza:
                # 1. La añadimos al catálogo del destino
                almacen_destino.catalogo_repuestos.append(repuesto)
                # 2. La eliminamos de nuestro almacén
                self.almacen_asignado.catalogo_repuestos.remove(repuesto)
                
                print(f"Operario {self.id_usuario}: Transferencia autorizada. '{nombre_pieza}' enviada a {almacen_destino.nombre}.")
                return True
            
            
            
def consultar_precio(self, nombre_pieza : str, almacenes_imperio : list ):
        ''' Para una pieza concreta, buscamos el precio que tiene y además, se devuelve la pieza con menor precio entre todas ellas.'''  
        precio_mas_bajo = float('inf')
        pieza_encontrada_con_stock = False
        pieza_existe = False # Añadimos esta bandera para saber si al menos la hemos visto
        repuesto_mas_barato = None

        for almacen in almacenes_imperio:
            for repuesto in almacen.catalogo_repuestos:
                if repuesto.get_nombre() == nombre_pieza:
                    pieza_existe = True # ¡Bingo! La pieza está en el catálogo, independientemente del stock
                    
                    if repuesto.get_cantidad_disponible() > 0:
                        pieza_encontrada_con_stock = True # Además de existir, hay stock
                        if repuesto.get_precio() < precio_mas_bajo:
                            precio_mas_bajo = repuesto.get_precio()
                            repuesto_mas_barato = repuesto.get_nombre()
        
        # 1ª EXCEPCIÓN: La pieza ni siquiera existe en ningún catálogo
        if not pieza_existe:
            raise PiezaNoEncontradaError(f"Fallo en la consulta: El repuesto '{nombre_pieza}' no existe en la base de datos del Imperio.")
            
        # 2ª EXCEPCIÓN: La pieza existe, pero el stock es 0 en todos los almacenes
        if not pieza_encontrada_con_stock:
             raise ErrorStockInsuficiente(f"Fallo en la consulta: El repuesto '{nombre_pieza}' existe, pero el stock es 0 en toda la galaxia.")

        # Si el código llega hasta aquí, es que existe y hay stock. Devolvemos el string.
        return f"Mejor precio {precio_mas_bajo}, para el repuesto {repuesto_mas_barato}"
    
# MEJORA: DEMOSTRAR EN EL MENÚ QUE EL COMANDANTE NO ÚNICAMENTE PUEDE VER UN OBJETO, SINO QUE PUEDE OBSERVAR UNA LISTA DE ELLOS:
# Esto iría en tu menú principal, fuera de las clases
lista_de_vader = ["Motor Iónico", "Condensador de Fluzo", "Cañón Láser"]

print("--- REPORTE DE DISPONIBILIDAD ---")

for pieza in lista_de_vader:
    try:
        # Llamamos a tu función estricta que solo mira 1 pieza
        comandante_vader.consultar_disponibilidad(pieza, almacenes_imperio)
        print(f"✅ {pieza}: Disponible y con stock.")
        
    except ErrorRepuestoNoEncontrado as e:
        print(f"❌ {pieza}: Error - No existe en los catálogos.")
        
    except ErrorStockInsuficiente as e:
        print(f"⚠️ {pieza}: Alerta - Existe, pero el stock es 0.")

print("---------------------------------")