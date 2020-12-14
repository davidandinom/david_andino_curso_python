"""Darwin favor analizar el programa y realizar tu comentario para ver que debo mejorar o que esta errado, 
y si se cumplio con el objetivo del trabajo.
Adicional favor probar el programa en los casos que pide id de producto, ingresar 1, ya que me falta validar 
los id de los productos existentes, entonces se realizó la prueba con el id 1
Agradezco tu ayuda y comentarios.
Saludos
"""

class Productos:
    
    def __init__(self, i_d, nombre_producto, grupo, subgrupo):
        self.i_d = i_d
        self.nombre_producto = nombre_producto
        self.grupo = grupo
        self.subgrupo = subgrupo

    def __str__(self):
        return 'Producto: id {} nombre {} grupo {} subgrupo {}'.format(self.i_d, self.nombre_producto, self.grupo, self.subgrupo)

class Admin (Productos):
    
    productos = []
    def __init__(self, i_d, nombre_admin):
        self.i_d = i_d
        self.nombre_admin = nombre_admin
        
    def __str__(self):
        return 'Administrador {} con id {}'.format(self.nombre_admin, self.i_d)

    def ver_productos (self):
        print ("Productos Existentes")
        for p in self.productos:
            print ("Existen los siguientes productos: ",p)
        pass
    def agregar_productos (self, producto):
        self.productos.append (producto)
        print ("Se agregó ",producto)

    def eliminar_productos (self,producto):
        if producto in self.productos:
            self.productos.remove(producto)
            print ("Se eliminó el ",producto)
        else:
            print ("El Producto no existe")

    def modificar_productos (self,producto):
        if producto in self.productos:
            print ("El producto a modificar si existe",producto)
            while True:
                print("""MENU MODIFICAR
                1.- I_D
                2.- NOMBRE_PRODUCTO
                3.- GRUPO
                4.- SUBGRUPO
                S.- Salir 
                """)
                opcion = input("Seleccione el valor a modificar: \n")

                if opcion == '1':
                    nuevo_id = int (input("Ingrese el nuevo valor de id: "))
                    producto.i_d = nuevo_id
                elif opcion == '2':
                    nuevo_nombre_producto = input("Ingrese el nuevo nombre del producto: ")
                    producto.nombre_producto = nuevo_nombre_producto
                elif opcion == '3':
                    nuevo_grupo = input("Ingrese el nuevo grupo del producto: ")
                    producto.grupo = nuevo_grupo
                elif opcion == '4':
                    nuevo_subgrupo = input("Ingrese el nuevo sugrupo del producto: ")
                    producto.subgrupo = nuevo_subgrupo
                elif opcion == 'S' or opcion == 's':
                    caracter = input("Desea salir de modificar: y/n \n")
                    if caracter == 'y' or caracter == 'Y':
                        break
                else:
                    pass
        else:
            print ("El producto no existe")

    def realizar_envio (self):
        print ("Se realizó envío a {} con direccion {} y teléfono {}".format(cliente_1.nombre_cliente, cliente_1.direccion, cliente_1.phno))

    def confirmar_entrega (self):
        print ("El cliente {} con id {}, confirma la entrega del producto {} y {}".format(cliente_1.nombre_cliente,cliente_1.id_cliente,producto_1,producto_2))

class Carro ():

    def __init__(self, id_cliente, numero_producto, producto_1, producto_2, precio, total):
        self.id_cliente = id_cliente
        self.numero_producto = numero_producto
        self.producto_1 = producto_1
        self.producto_2 = producto_2
        self.precio = precio
        self.total = total

    def __str__(self):
        return 'cliente con id {} número de producto {} producto 1 {} producto 2 {}, precio {}, total {}'.format(self.id_cliente, self.numero_producto, self.producto_1, self.producto_2, self.precio, self.total)
class Cliente (Admin, Carro):
    clientes = []
    cesta = []
    def __init__(self, id_cliente, nombre_cliente, direccion, phno):
        self.id_cliente = id_cliente
        self.nombre_cliente = nombre_cliente
        self.direccion = direccion
        self.phno = phno

    def __str__(self):
        return 'cliente con id {} nombre {} direccion {} phno {}'.format(self.id_cliente, self.nombre_cliente, self.direccion, self.phno)

    def comprar_productos (self):
        compra = input ("Desea compar los productos (Ingresar s o S): ")
        if compra == 's' or compra == 'S':
            print ("El cliente con id {} va a pagar por {} productos el precio sin iva {} y valor total con iva {}".format(carro_cliente_1.id_cliente,carro_cliente_1.numero_producto,carro_cliente_1.precio,carro_cliente_1.total))
            print ("Los productos comprados son: {} y {}".format(producto_1,producto_2))
            print ("Continuar el pago")
        else:
            print ("Se volvera a mostrar su cesta")

    # def ver_productos (self): Este metodo se hereda de la clase admin
    
    def realizar_pago (self):
        print ("El pago se realizó con éxito:")
        print ("El cliente {} con id {}  pagó con tarjeta {} numero {} el valor de {}". format(pago_cliente_1.identificador_cliente,pago_cliente_1.nombre_cliente,pago_cliente_1.tipo_tarjeta,pago_cliente_1.no_tarjeta,carro_cliente_1.total))

    def anadir_cesta (self):
        #Falta añadir líneas de codigo para realizar comparación de id de acuerdo a productos existentes
        #como ejemplo se realiza del producto 1
        print ("Escoger productos por id de la lista de productos existentes para añadir a la cesta:")
        id_productos = int (input ("Ingrese id del producto: "))
        self.cesta.append(id_productos)
        print (self.cesta)
        self.productos[0]
        print ("El cliente {} con id {} añadió a la cesta el {}".format(cliente_1.nombre_cliente, cliente_1.id_cliente,self.productos[0]))

    def borrar_cesta (self):
        #pendiente validar y los productos de la cesta para eliminar los que desea
        print ("Escoger el id de la de productos de la cesta a eliminar:")
        id_productos = int (input ("Ingrese id del producto: "))
        #print (self.cesta)
        self.cesta.remove(self.cesta[0])
        print ("El cliente {} con id {} borro de la cesta el {}".format(cliente_1.nombre_cliente, cliente_1.id_cliente,self.productos[0]))
        #print (self.cesta)
        print ("Cesta Eliminada")

class Pago (Cliente):
    
    def __init__(self, identificador_cliente, nombre_cliente, tipo_tarjeta, no_tarjeta):
        self.identificador_cliente = identificador_cliente
        self.nombre_cliente = nombre_cliente
        self.tipo_tarjeta = tipo_tarjeta
        self.no_tarjeta = no_tarjeta

    def __str__(self):
        return 'El cliente {}  con nombre {} tipo de tarjeta {} no_tarjeta {}'.format(self.identificador_cliente, self.nombre_cliente, self.tipo_tarjeta, self.no_tarjeta)

class Invitado (Admin):
    
    def __init__(self):
        print ("Es un invitado")
    
    #def ver_productos (self):  Metodo heredado de clase Admin

    def registrarse (self):
        print ("Hola, usted se registró como invitado")

if __name__ == "__main__":

    #Creación de productos
    producto_1 = Productos(1,'Colonia Spiderman','Fragancia','Niños')
    producto_2 = Productos(2,'Colonia Rayo Mcqueen','Fragancia','Niños')
    producto_3 = Productos(3,'Colonia Advengers','Fragancia','Niños')
    producto_4 = Productos(4,'Colonia Blaze','Fragancia','Niños')
    producto_5 = Productos(5,'Colonia Frozen','Fragancias','Niños')
    #Llamar a la Clase Admin
    administrador_1 = Admin (1,'David')
    #Agregar Productos
    administrador_1.agregar_productos(producto_1)
    administrador_1.agregar_productos(producto_2)
    administrador_1.agregar_productos(producto_3)
    administrador_1.agregar_productos(producto_4)
    administrador_1.agregar_productos(producto_5)
    #MostrarProductos
    administrador_1.ver_productos()
    #Eliminar Productos
    administrador_1.eliminar_productos(producto_3)
    administrador_1.ver_productos()
    #Modificar Productos, Pendiente validar datos ingresados en la solicitud de modificaciones
    administrador_1.modificar_productos(producto_5)
    administrador_1.ver_productos()
    #Crear Cliente
    cliente_1 = Cliente ('1','Tatiana Tapia','Quito','0998925260')
    cliente_2 = Cliente ('2','Tatiana Tapia 1','Quito','0998925260')
    #Ver Producto Cliente, ejemplo realizado con cliente_1
    print ("El cliente {} con id {} mira los productos existentes:".format(cliente_1.nombre_cliente, cliente_1.id_cliente))
    cliente_1.ver_productos()
    #Añadir Productos a la cesta. Escoger como ejemplo el id 1
    cliente_1.anadir_cesta()
    #Borrar Cesta. Escoger ejemplo el id 1
    cliente_1.borrar_cesta()
    #Añadir Productos a la cesta. Escoger como ejemplo el id 1
    cliente_1.anadir_cesta()
    #compra productos
    carro_cliente_1 = Carro ('1',2,producto_1, producto_2,350,350+(350*12/100))
    cliente_1.comprar_productos()
    #Realizar pago
    pago_cliente_1 = Pago ('1','Tatiana Tapia', 'Débito', '123456789')
    pago_cliente_1.realizar_pago()
    #Realizar envio de productos
    cliente_1.realizar_envio()
    #Confirmar entrega de productos
    cliente_1.confirmar_entrega()
    #Registro de invitador
    invitado = Invitado ()
    invitado.registrarse()
    #Ver productos como invitado
    invitado.ver_productos()