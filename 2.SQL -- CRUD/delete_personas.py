import mysql.connector;

conexion = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="mydb",
)

cursor = conexion.cursor()

consulta = "DELETE FROM personas WHERE id_personas=%s;"
valores = (4,) #la coma es para identificarlo como tupla

cursor.execute(consulta, valores)
conexion.commit()

print("Se ha eliminado la información correctamente")

cursor.close()
conexion.close()