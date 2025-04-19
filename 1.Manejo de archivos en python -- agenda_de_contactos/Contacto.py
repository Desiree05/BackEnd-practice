class Contacto:

    def __init__(self, nombre='', telefono=0, email=''):
        if not len(str(telefono)) == 9:
            print("ERROR: al crear un contacto con un teléfono que no tiene 9 dígitos")
            return

        if email.find("@") == -1:
            print("ERROR: al crear un contacto con un email que no tiene @")
            return 
        
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Contacto con nombre: {self.nombre}, teléfono: {self.telefono}, email: {self.email}"

    # En el fichero
    def escribir_contacto(self):
        return f"{self.nombre},{self.telefono},{self.email}\n"
    
    

        
