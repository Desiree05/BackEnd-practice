import mysql.connector;

conexion = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="mydb",
)

cursor = conexion.cursor()

consulta = "UPDATE personas SET DNI=%s, nombre=%s, salario=%s WHERE id_personas=%s;"
valores = ("12345678M", "Pepe Juan", 12345.588, 4)

cursor.execute(consulta, valores)
conexion.commit()

print("Se ha modificado la información correctamente")

cursor.close()
conexion.close()
