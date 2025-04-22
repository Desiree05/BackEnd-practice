class Producto:

    def __init__(self, id=None, nombre=None, cantidad=None, precio=None, categoria=None):
        if nombre == None or cantidad == None or precio == None or categoria == None:
            print("ERROR: al crear un producto ya que algún valor no se ha inicializado")
            return
        
        if precio < 0:
            print(f"ERROR: al crear un producto con un precio negativo --> {precio}")
            return

        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio
        self.categoria = categoria 

    def __str__(self):
        return f"Contacto con nombre: {self.nombre}, cantidad: {self.cantidad}, precio: {self.precio}, categoria: {self.categoria}"

    
    

        
