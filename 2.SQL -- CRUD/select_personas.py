import mysql.connector;

conexion = mysql.connector.connect(
    host="localhost", # 127.0.0.1
    user="root",
    password="admin",
    database="mydb",
)

cursor = conexion.cursor()

consulta_SELECT = "SELECT * FROM personas;"
cursor.execute(consulta_SELECT)

resultados = cursor.fetchall()

for fila in resultados:
    print(fila)

cursor.close()
conexion.close()
