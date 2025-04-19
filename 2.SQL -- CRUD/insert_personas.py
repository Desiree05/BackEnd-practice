import mysql.connector;

conexion = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="mydb",
)

cursor = conexion.cursor()

consulta = "INSERT INTO personas (DNI, nombre, salario) VALUES (%s, %s, %s);"
valores = ("12345678M", "Pepe", 123456.78)

cursor.execute(consulta, valores)
conexion.commit()

print("Pepe añadido")

cursor.close()
conexion.close()
