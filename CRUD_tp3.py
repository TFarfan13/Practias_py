import json
from datetime import datetime

class Producto:
    def __init__(self, id_producto, nombre, precio, fecha_vencimiento, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.fecha_vencimiento = fecha_vencimiento
        self.cantidad = cantidad
        
    def to_dict(self):
        return {
            "id_producto": self.id_producto,
            "nombre": self.nombre,
            "precio": self.precio,
            "fecha_vencimiento": self.fecha_vencimiento.strftime('%m/%Y'),
            "cantidad": self.cantidad
        }

class Inventario:
    def __init__(self, archivo):
        self.archivo = archivo
        try:
            with open(archivo, "r") as file:
                self.productos = json.load(file)
        except FileNotFoundError:
            self.productos = {}

    def añadir_prod(self,producto):
        if producto.id_producto in self.productos:
            print(f"El producto con ID {producto.id_producto} ya existe en el inventario.")
        else:
            self.productos['producto.id_producto'] = producto.to_dict()
            self.guardar()
            print(f"Producto {producto.nombre} añadido con éxito.")
            
    def guardar(self):
        with open(self.archivo, "w") as file:
            json.dump(self.productos, file, indent=4)
    
    def actualizar(self, id_producto, nombre=None, precio=None, fecha_vencimiento=None, cantidad=None):
        if id_producto in self.productos:
            if nombre is not None:
                self.productos[id_producto]['nombre'] = nombre
            if precio is not None:
                self.productos[id_producto]['precio'] = precio
            if fecha_vencimiento is not None:
                self.productos[id_producto]['fecha_vencimiento'] = fecha_vencimiento.strftime('%m/%Y')
            if cantidad is not None:
                self.productos[id_producto]['cantidad'] += cantidad
            self.guardar()
            print(f"Producto {id_producto} actualizado.")
        else:
            print("Producto no encontrado")
            
    def eliminar_producto(self,id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            self.guardar()
            print("Producto eliminado con exito")
            
    def mostrar_producto(self, id_producto):
        if id_producto in self.productos:
            producto = self.productos[id_producto]
            print(f"ID: {id_producto}\n"
                  f"Nombre: {producto['nombre']}\n"
                  f"Precio: {producto['precio']}\n"
                  f"Fecha de Vencimiento: {producto['fecha_vencimiento']}\n"
                  f"Cantidad: {producto['cantidad']}")  
        else:
            print("Producto no encontrado en el inventario.")

def solicitar_datos_producto():
    print("INVENTARIADO DE PRODUCTOS")
    
    print("Ingrese datos del nuevo producto")
    

    while True:
        try:
            id_producto = input("ID del producto: ")
            if id_producto.isnumeric():
                break
            else:
                raise ValueError("Ingrese un ID válido")
        except ValueError as error:
            print(error)
    print(f"El ID ingresado es: {id_producto}")

    while True:
        try:
            nombre = input("Nombre del producto: ")
            if nombre.isalpha():
                break
            else:
                raise ValueError("Ingrese un nombre válido")
        except ValueError as error:
            print(error)
    print(f"El nombre ingresado es: {nombre}")       

    while True:
        try:
            precio = float(input("Ingrese el precio: "))
            break
        except ValueError:
            print("Por favor, ingrese un precio válido.")
    print(f"El precio ingresado es: {precio}")

    while True:
        fecha_vencimiento = input("Ingrese fecha de vencimiento (mm/yyyy): ")
        try:
            fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%m/%Y")
            break
        except ValueError:
            print("Por favor, ingrese una fecha válida en el formato mm/yyyy.")
    print(f"La fecha de vencimiento ingresada es: {fecha_vencimiento.strftime('%m/%Y')}")

    while True:
        try:
            cantidad = int(input("Cantidad: "))
            break
        except ValueError:
            print("Por favor, ingrese una cantidad válida.")
    
    return Producto(id_producto, nombre, precio, fecha_vencimiento, cantidad)

def menu():
    inventario = Inventario('inventario.json')
    
    while True:
        print("\nMenú de opciones:")
        print("1. Añadir producto")
        print("2. Actualizar producto")
        print("3. Mostrar producto")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            producto = solicitar_datos_producto()
            inventario.añadir_prod(producto)
        elif opcion == "2":#Por cuestiones de tiempo no llegue a agregar try and except para posibles erroes en los input
            id_producto = input("Ingrese el ID del producto a actualizar: ")
            print("Deje en blanco los campos que no quiera actualizar")
            nombre = input("Ingrese el nuevo nombre (o presione Enter para dejar sin cambios): ")
            precio = input("Ingrese el nuevo precio (o presione Enter para dejar sin cambios): ")
            fecha_vencimiento = input("Ingrese la nueva fecha de vencimiento (mm/yyyy) (o presione Enter para dejar sin cambios): ")
            cantidad = input("Ingrese la cantidad a añadir (o presione Enter para dejar sin cambios): ")
            
            nombre = nombre if nombre else None
            precio = float(precio) if precio else None
            fecha_vencimiento = datetime.strptime(fecha_vencimiento, "%m/%Y") if fecha_vencimiento else None
            cantidad = int(cantidad) if cantidad else None
            
            inventario.actualizar(id_producto, nombre, precio, fecha_vencimiento, cantidad)
            
        elif opcion == "3":
            id_producto = input("Ingrese el ID del producto a mostrar: ")
            inventario.mostrar_producto(id_producto)

               
        elif opcion== "4":
            id_producto=input("Por favor Ingrese l ID del producto a eliminar")
            print(f"Va a eliminar el producto {id_producto}")
            inventario.mostrar_producto(id_producto)
            print("Que desea hacer ?")
            print("1.Eliminar")
            print("2.Cancelar")
            opcion=input("Ingrese opcion")
            if opcion=="1":
                inventario.eliminar_producto(id_producto)
                
            elif opcion=="2":
                menu()
            
        
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción del menú.")

if __name__ == "__main__":
    menu()
