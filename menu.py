#! /usr/bin/python3
from persona import Persona
from listado import Listado
import sys
class Menu:
    '''Mostrar un menú y responder a las opciones'''

    def __init__(self):
        self.listado = Listado()

    def mostrar_menu(self):
        '''Muestra el menú de opciones'''
        print("""
Menú del anotador:
1. Mostrar todas las personas
2. Agregar persona
3. Modificar datos de una persona
4. Eliminar persona de la lista
5. Salir
""")

    def ejecutar(self):
        '''Mostrar el menu y responder a las opciones.'''
        while True:
            self.mostrar_menu()
            opcion = int(input("Ingresar una opción: "))

            # Guardamos en la variable accion el método que corresponde a la
            # opción elegida por el usuario. Por ejemplo, si opcion tiene el 
            # valor 1, accion va a guardar el valor correspondiente a 
            # self.opciones[1], es decir: self.mostrar_notas
            # accion = self.opciones.get(opcion)
            if opcion == 1:
                self.mostrar_personas()
            elif opcion == 2:
                self.agregar_persona()
            elif opcion == 3:
                self.modificar_datos_persona()
            elif opcion == 4:
                self.eliminar_persona()
            elif opcion == 5:
                self.salir()
            else:
                print("No es una opción válida")

    def mostrar_personas(self):
        '''Muestra todas las personas del listado'''
        print(self.listado)

    def agregar_persona(self):
        '''Solicita los valores al usuario y agrega una nueva persona'''
        d = input("Ingrese el dni de la persona: ")
        n = input("Ingrese el nombre de la persona: ")
        a = input("Ingrese el apellido: ")
        fn = input("Ingrese la fecha de nacimiento (dia/mes/año): ")
        fn = fn.split('/')

        self.listado.nueva_persona(d, n, a, int(fn[0]), int(fn[1]), int(fn[2]))

    def modificar_datos_persona(self):
        self.mostrar_personas()
        d = input("Ingrese el dni de la persona: ")
        print("Si no desea modificar alguno de los datos, déjelo en blanco")
        n = input("Ingrese el nuevo nombre de la persona: ")
        a = input("Ingrese el nuevo apellido de la persona: ")
        fn = input("Ingrese la nueva fecha de nacimiento (dia/mes/año): ")
        if len(fn) > 0:
            fn = fn.split('/')
            self.listado.modificar_datos(d, n, a, int(fn[0]), int(fn[1]), int(fn[2]))
        else:
            self.listado.modificar_datos(d, n, a, 0, 0, 0)

    def eliminar_persona(self):
        self.mostrar_personas()
        d = input("Ingrese el dni de la persona: ")
        self.listado.eliminar_persona(d)

    def salir(self):
        '''Muestra un mensaje y sale del sistema'''
        print("Gracias por utilizar el sistema.")
        sys.exit(0)

#Esta parte del código está fuera de la clase Menu.
#Si este archivo es el programa principal (es decir, si no ha sido importado
#desde otro módulo, sino ejecutado directamente), entonces llamamos al método
# ejecutar(). 
if __name__ == "__main__":
    Menu().ejecutar()
