from producto import Producto

class Tienda():
    #constructor 
    def __init__(self,nombre: str, costo_delivery: int,tipo: str):
        self.__nombre = nombre
        self.__costo_delivery = costo_delivery
        self.__productos = []
        self.__tipo = tipo
    
        
    @property     
    def nombre(self):
        return self.__nombre
    
    @property
    def costo_delivery(self):
        return self.__costo_delivery
    
    def agregar_producto(self):
        
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        stock = int(input("Ingrese el stock del producto: "))
        
        if self.__tipo == "Restaurante":
            # stock cero para restaurante
            stock = 0

        producto = Producto(nombre, precio, stock)
        
        for p in self.__productos:
            if p.nombre == producto.nombre:
                # sumando al stock
                p.stock += producto.stock
                print("Producto ya existente, se ha actualizado el stock.")
                return
        
        # añadir producto
        self.__productos.append(producto)
        print("Producto ingresado exitosamente.")  
        
        
    def listar_productos(self):
        lista_productos = "Productos existentes en la tienda:\n"
        # iterando
        if self.__tipo == "Restaurante":
            for producto in self.__productos:
                lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}\n"
        else:
            for producto in self.__productos:
                lista_productos += f"Nombre: {producto.nombre}, Precio: {producto.precio}"
                 #condicionales
                if self.__tipo == "Supermercado":
                    if producto.stock < 10:
                        lista_productos += " - Pocos productos disponibles"
                #condiocnales farmacia
                elif self.__tipo == "Farmacia":
                    if producto.precio > 15000:
                        lista_productos += " - Envío gratis al solicitar este producto"
               
        return lista_productos
    
    def realizar_venta(self, nombre_producto: str, cantidad: int):
        print("Realizando venta...")  
        if self.__tipo == "Restaurante":
            print("Venta realizada exitosamente.")
            return
        for producto in self.__productos:
            if producto.nombre == nombre_producto:
                if self.__tipo == "Farmacia" and cantidad > 3:
                 
                    print("No se puede vender más de 3 unidades en Farmacia.")
                    return
                if cantidad <= producto.stock:
                    
                    producto.stock -= cantidad
                    print("Venta realizada exitosamente.")  
                    return
                else:
                    
                    print("No hay suficiente stock para la venta.")
                    return

        print("El producto solicitado no está disponible en la tienda.")