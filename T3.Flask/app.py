from flask import Flask, render_template
from ProductoDAO import ProductoDAO

app = Flask(__name__)

titulo_app = "Almacén"

@app.route("/") #url: http://localhost:5000/
@app.route("/index.html") #url: http://localhost:5000/index.html
def inicio():
    app.logger.debug("Entrando al path de inicio /")

    # Recuperamos los productos de la Base de Datos
    productos_db = ProductoDAO.seleccionar()
    
    return render_template("index.html", titulo=titulo_app, productos=productos_db)    # Mira en la carpeta "templates"
#puedes ir añadiendo parametros poniendole los nombres que quieras 


if __name__ == "__main__":
    app.run(debug=True)     # para poder ver los cambios de manera automática + loger.debug