from ProductoDAO import ProductoDAO
from Producto import Producto

print("*** ¡Hola bienvenido al almacén! ***")
opcion = None

while opcion != 5:
    print("""\n¿Qué acción quieres realizar? 
        1. Listar productos
        2. Agregar producto
        3. Modificar producto
        4. Eliminar producto
        5. Salir""")
    
    try:

        opcion = int(input("Selecciona un número del 1-5: "))

        if opcion == 1:     #Listar productos
            productos = ProductoDAO.seleccionar()
            print(f"\n*** Listado de Productos***")

            for producto in productos:
                print(producto)

        elif opcion == 2:   #Agregar producto
            nombre = str(input("¿Cuál es el nombre del producto? "))
            cantidad = int(input("¿Cuál es su cantidad? "))
            precio = float(input("¿Cuál es su precio? "))
            categoria = str(input("¿Cuál es su categoría? "))

            producto = Producto(nombre=nombre, cantidad=cantidad, precio=precio, categoria=categoria)

            productos_insertados = ProductoDAO.insertar(producto)

            if productos_insertados != 0:
                print(f"¡Producto {nombre} agregado con éxito!")
            else:
                print(f"No se pudo agregar el producto {nombre}, {productos_insertados} productos insertados.")


        elif opcion == 3:   #Modificar producto
            id = int(input("¿Cuál es el id actual del producto a modificar? "))
            nombre = str(input("¿Cuál será el nombre del producto nuevo? "))
            cantidad = int(input("¿Cuál será su cantidad nueva? "))
            precio = float(input("¿Cuál será su precio nuevo? "))
            categoria = str(input("¿Cuál será su categoría nueva? "))

            producto = Producto(id, nombre, cantidad, precio, categoria)

            productos_actualizados = ProductoDAO.actualizar(producto)

            if productos_actualizados != 0:
                print(f"¡Producto {nombre} actualizado con éxito!")
            else:
                print(f"No se pudo actualizar el producto {nombre}, {productos_actualizados} productos actualizado.")

        elif opcion == 4:   #Eliminar producto
            id = int(input("¿Cuál es el id del producto que quieres eliminar? "))

            productos_eliminados = ProductoDAO.eliminar(id)

            if productos_eliminados != 0:
                print(f"¡Producto con id {id} eliminado con éxito!")
            else:
                print(f"No se pudo eliminar el producto {id}, {productos_eliminados} productos eliminados.")

        elif opcion == 5:
            print("¡Qué tengas un buen día! =)")

    except ValueError as e:
        print(f"Valor incorrecto, los valores a insertar son: id = número, nombre = caracteres, cantidad = número, precio = decimal, categoria = caracteres")