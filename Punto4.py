class Nodo:
    def __init__(self, nombre_producto, monto_compra):
        self.nombre_producto = nombre_producto
        self.monto_compra = monto_compra
        self.siguiente = None

class ListaProductos:
    def __init__(self):
        self.cabeza = None

    def agregar_producto(self, nombre_producto, monto_compra):
        nuevo_nodo = Nodo(nombre_producto, monto_compra)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def mostrar_producto(self):
        actual = self.cabeza
        while actual:
            print(f"Producto: {actual.nombre_producto}, Precio: {actual.monto_compra}")
            actual = actual.siguiente

    def total_compras(self):
        total = 0
        actual = self.cabeza
        while actual:
            total += actual.monto_compra
            actual = actual.siguiente
        return total

    def obtener_informacion_producto(self):
        nombre_producto = input("Ingrese el nombre del producto: ")
        while True:
            try:
                monto_compra = float(input("Ingrese el precio del producto: "))
                if monto_compra >= 0:
                    break
                else:
                    print("El monto de la compra no puede ser negativo. Ingrese un valor positivo.")
            except ValueError:
                print("Valor inválida. Solo se aceptan numeros")
        return nombre_producto, monto_compra

def main():
    lista_productos = ListaProductos()

    while True:
        agregar_mas = input("¿Desea agregar otro producto? (si/no): ")
        if agregar_mas.lower() != 'si':
            break

        nombre_producto, monto_compra = lista_productos.obtener_informacion_producto()
        lista_productos.agregar_producto(nombre_producto, monto_compra)

    lista_productos.mostrar_producto()

    total_compras = lista_productos.total_compras()
    print(f"Total de compras: ${total_compras:.2f}")

if __name__ == "__main__":
    main()
