from Contacto import Contacto
from os.path import os;


class servicio_agenda:

    def __init__(self):

        # Para añadir parametros del objeto poner self.
        self.lista_contactos = []
        self.nombre_archivo = "agenda_de_contactos/contactos.txt"

        if os.path.isfile(self.nombre_archivo):        
            with open(self.nombre_archivo, "r") as archivo:
                for linea in archivo:
                    contacto = linea.split(",")
                    self.lista_contactos.append(Contacto(contacto[0], int(contacto[1]), contacto[2]))
        else:
            self.lista_contactos = [Contacto("Paco", 123456789, "paco@gmail.com")]
            self.add_contacto(self.lista_contactos[0])


    
    
    def add_contacto(self, contacto=Contacto):
        try:
            self.lista_contactos.append(contacto)
            with open(self.nombre_archivo, "a") as archivo:
                    archivo.write(Contacto.escribir_contacto(contacto))
                    print(f"Escribiendo en fichero {self.nombre_archivo} el contacto {contacto.nombre}")
        except ValueError as e:
                print(f"ERROR: No se pudo añadir el contacto. {e}")

    def listado_contactos(self):
        for contacto in self.lista_contactos:
            print(contacto.__str__().strip())

    # Devuelve el index del contacto si lo encuentra, -1 si no lo encuentra
    def buscar_contacto_by_telefono(self, telefono):

        for index, contacto in enumerate(self.lista_contactos):
            if contacto.telefono == telefono:
                print(contacto.__str__().strip())
                print(f"Contacto encontrado en la posición {index}")
                return index
        return -1

    def borrar_contacto_by_telefono(self, telefono):

        index = self.buscar_contacto_by_telefono(telefono)

        if index != -1:
            del self.lista_contactos[index]
            with open(self.nombre_archivo, "w") as archivo:
                for index,contacto in enumerate(self.lista_contactos):
                    if contacto != None:
                        archivo.write(Contacto.escribir_contacto(contacto).strip() + "\n")

        # TODO: cuando borras un contacto que está en el medio deja el hueco en vez de subir todos



        return index





             


        