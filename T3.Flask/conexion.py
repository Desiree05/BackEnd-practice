# Clase para crear el pool de conexiones

from mysql.connector import pooling
from mysql.connector import Error

class Conexion:
    DATABASE = "almacen_db"
    USERNAME = "root"
    PASSWORD = "1234"
    HOST = "localhost"
    POOL_SIZE = 5
    POOL_NAME = "almacen_pool"
    pool = None

    @classmethod
    def obtener_pool(cls):  #cls = como self.Conexion
        if cls.pool is None:
            try:
                cls.pool = pooling.MySQLConnectionPool(
                    pool_name= cls.POOL_NAME,
                    pool_size= cls.POOL_SIZE,
                    host= cls.HOST,
                    port= cls.DB_PORT,
                    database=cls.DATABASE,
                    user= cls.USERNAME,
                    password= cls.PASSWORD
                )

                return cls.pool
            except Error as e:
                print(f"Ocurrio un error al obtener el pool de conexiones: {e}")
            
        else:
            return cls.pool
        

    
    # Lo que establece conexion al usuario    
    @classmethod
    def obtener_conexion(cls):
        return cls.obtener_pool().get_connection()
    

    # Lo que rompe conexion al usuario    
    @classmethod
    def liberar_conexion(cls, conexion):
        conexion.close()



if __name__ == '__main__':
    pool = Conexion.obtener_pool()
    print(pool)

    conexion1 = pool.get_connection()
    print(conexion1)

    Conexion.liberar_conexion(conexion1)

    print("Se ha liberado el objeto conexion1")

