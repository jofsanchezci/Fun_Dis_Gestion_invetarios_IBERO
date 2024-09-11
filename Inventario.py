class Producto:
    def __init__(self, nombre, cantidad, umbral_alerta):
        self.nombre = nombre
        self.cantidad = cantidad
        self.umbral_alerta = umbral_alerta

    def actualizar_cantidad(self, nueva_cantidad):
        self.cantidad = nueva_cantidad
        self.verificar_alerta()

    def verificar_alerta(self):
        if self.cantidad < self.umbral_alerta:
            print(f"ALERTA: El producto '{self.nombre}' está bajo en stock (Cantidad actual: {self.cantidad})")


class GestionInventarios:
    def __init__(self):
        self.inventario = {}

    def agregar_producto(self, nombre, cantidad, umbral_alerta):
        if nombre not in self.inventario:
            producto = Producto(nombre, cantidad, umbral_alerta)
            self.inventario[nombre] = producto
            print(f"Producto '{nombre}' agregado con {cantidad} unidades.")
        else:
            print(f"El producto '{nombre}' ya existe en el inventario.")

    def actualizar_stock(self, nombre, nueva_cantidad):
        if nombre in self.inventario:
            producto = self.inventario[nombre]
            producto.actualizar_cantidad(nueva_cantidad)
            print(f"Cantidad actualizada para '{nombre}'. Nueva cantidad: {nueva_cantidad}.")
        else:
            print(f"El producto '{nombre}' no existe en el inventario.")

    def generar_reporte(self):
        print("Reporte de Inventario:")
        for nombre, producto in self.inventario.items():
            print(f"Producto: {nombre}, Cantidad: {producto.cantidad}, Umbral de alerta: {producto.umbral_alerta}")

# Ejemplo de uso del prototipo
if __name__ == "__main__":
    gestion_inventarios = GestionInventarios()

    print('--------------------------------------------')
    print('--------------------------------------------')
    print('Agrerar Producto')

    # Agregar productos al inventario
    gestion_inventarios.agregar_producto("Laptop", 10, 5)
    gestion_inventarios.agregar_producto("Mouse", 50, 20)
    gestion_inventarios.agregar_producto("Teclado", 234, 50)
    gestion_inventarios.agregar_producto("Monitor", 344, 50)
    print('--------------------------------------------')
    print('--------------------------------------------')
    print('Actualizar Producto')

    # Actualizar stock y verificar alertas
    gestion_inventarios.actualizar_stock("Laptop", 4)
    gestion_inventarios.actualizar_stock("Mouse", 19)
    print('--------------------------------------------')
    print('--------------------------------------------')
    print('Generar Reporte')


    # Generar un reporte del inventario
    gestion_inventarios.generar_reporte()

