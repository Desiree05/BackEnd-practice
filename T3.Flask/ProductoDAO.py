from conexion import Conexion
from Producto import Producto


class ProductoDAO:
    SELECCIONAR = "SELECT * FROM almacen ORDER BY id;"
    INSERTAR = "INSERT INTO almacen(nombre, cantidad, precio, categoria) VALUES (%s, %s, %s, %s);"
    ACTUALIZAR = "UPDATE almacen SET nombre=%s, cantidad=%s, precio=%s, categoria=%s WHERE id=%s;"
    ELIMINAR = "DELETE FROM almacen WHERE id=%s;"


    @classmethod
    def seleccionar(cls):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()
            cursor.execute(cls.SELECCIONAR)
            registros = cursor.fetchall()

            # Recuperarlos como objeto Producto
            productos = []
            for registro in registros:
                producto = Producto(registro[0], registro[1], registro[2], registro[3], registro[4])
                productos.append(producto)

            return productos

        except Exception as e:
            print(f"Error al seleccionar producto del alamacen {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def insertar(cls, producto=Producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria)
         
            cursor.execute(cls.INSERTAR, valores)
            conexion.commit()

            return cursor.rowcount #nº de valores que se inserto

        except Exception as e:
            print(f"Error al insertar un producto del alamacen: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



    #Poner el id del producto que quieres insertar
    @classmethod
    def actualizar(cls, producto=Producto):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (producto.nombre, producto.cantidad, producto.precio, producto.categoria, producto.id)
         
            cursor.execute(cls.ACTUALIZAR, valores)
            conexion.commit()

            return cursor.rowcount #nº de valores que se modifico

        except Exception as e:
            print(f"Error al actualizar un producto del alamacen: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)


    @classmethod
    def eliminar(cls, id):
        conexion = None
        try:
            conexion = Conexion.obtener_conexion()
            cursor = conexion.cursor()

            valores = (id,)
         
            cursor.execute(cls.ELIMINAR, valores)
            conexion.commit()

            return cursor.rowcount #nº de valores que se elimino

        except Exception as e:
            print(f"Error al eliminar un producto del alamacen: {e}")
        finally:
            if conexion is not None:
                cursor.close()
                Conexion.liberar_conexion(conexion)



if __name__ == "__main__":

    #productos_eliminados = ProductoDAO.eliminar(7)
    #print(f"Productos eliminados: {productos_eliminados}")
    
    productos = ProductoDAO.seleccionar()
    for producto in productos:
        print(producto) 
