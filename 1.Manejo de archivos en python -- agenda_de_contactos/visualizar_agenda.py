from servicio_agenda import servicio_agenda
from Contacto import Contacto

class visualizar_agenda:

    def __init__(self):
        self.servicio_agenda = servicio_agenda()


    def visualizador(self):

        try:
            salir = False

            while not salir:

                print("\n0: si quieres agregar un contacto")
                print("1: si quieres ver lista de contactos")
                print("2: si quieres buscar un contacto con su número de teléfono")
                print("3: si quieres borrar un contacto con su número de teléfono")
                print("4: si quieres salir de la agenda")

                valor = int(input())
                if valor == 0:
                    self.agregar_contacto()
                elif valor == 1:
                    self.listado_contactos()
                elif valor == 2:
                    self.buscar_contacto()
                elif valor == 3:
                    self.borrar_contacto()
                elif valor == 4:
                    print("¡Que tenga un buen día!")
                    salir = True
                else:
                    print("ERROR: select a number between 0 and 4")
        except ValueError:
            print("ERROR: Incorrect inputs, expecting an integer.")

    def agregar_contacto(self):

        nombre = str(input("Inserte el nombre del contacto a agregar: "))
        telefono = int(input("Inserte el telefono del contacto a agregar: "))
        email = str(input("Inserte el email del contacto a agregar: "))
        
        try:
            contacto = Contacto(nombre, telefono, email)        
            self.servicio_agenda.add_contacto(contacto)
            print(f"Contacto {nombre} añadido con éxito")
        except:
            print("ERROR: No se ha podido crear el contacto")
        

    def listado_contactos(self):
        self.servicio_agenda.listado_contactos()
    

    def buscar_contacto(self):
        telefono = int(input("Inserte el telefono del contacto a buscar: "))

        if self.servicio_agenda.buscar_contacto_by_telefono(telefono) != -1:
            print(f"Contacto {telefono} encontrado con éxito")
        else:
            print("That contact does not exist")

        

    def borrar_contacto(self):
        telefono = int(input("Inserte el telefono del contacto a borrar: "))
        if self.servicio_agenda.borrar_contacto_by_telefono(telefono) != -1:
            print(f"Contacto {telefono} borrado con éxito")
        else:
            print("That contact does not exist")


if __name__ == "__main__":

    visor = visualizar_agenda()
    visor.visualizador()
