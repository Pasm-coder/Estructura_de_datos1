class Digiturno:
    def __init__(self):
        self.clientes =[]
        self.capacidad_maxima = 4

    def vacio(self):
        return len(self.clientes) == 0
    
    def agregar(self, nodo):
        if len(self.clientes) < self.capacidad_maxima:
            self.clientes.append(nodo)
            print("La persona fue agregada a la cola ")
        else:
            print("La cola esta llena, espere a que se vacie para agregar otra persona")
    
    def eliminar(self):
        if self.vacio():
            print("La cola esta vacia")
        else:
            eliminado = self.clientes.pop(0)
            print("Eliminado: " + str(eliminado))

    def consultar(self):
        if self.vacio():
            print("La cola esta vacia")
        else:
            print(self.clientes)

obj = Digiturno()
while True:
    print("1. Insertar nombre")
    print("2. Consultar cola")
    print("3. Eliminar")
    print("4. Salir")
    opcion = int(input("Escribe tu opcion: "))
    if opcion == 1:
        nodo = input("Escriba el nombre de la persona: ")
        obj.agregar(nodo)
    elif opcion == 2:
        obj.consultar()
    elif opcion == 3:
        obj.eliminar()
    elif opcion == 4:
        break
    else:
        print("La opcion seleccionada no existe")
