from flask import Flask, render_template, redirect, url_for

from ProductoDAO import ProductoDAO
from Producto import Producto
from producto_forma import ProductoForma

app = Flask(__name__)

app.config["SECRET_KEY"] = "evitando_CSRF"

titulo_app = "Almacén"

@app.route("/") #url: http://localhost:5000/
@app.route("/index.html") #url: http://localhost:5000/index.html
def inicio():
    app.logger.debug("Entrando al path de inicio /")

    # Recuperamos los productos de la Base de Datos
    productos_db = ProductoDAO.seleccionar()

    # Creamos un objeto de producto forma
    producto = Producto()
    producto_forma = ProductoForma(obj=producto)    # para enlazar producto en el formulario
    
    return render_template("index.html", titulo=titulo_app, productos=productos_db, forma=producto_forma)    

    # Mira en la carpeta "templates"
    # puedes ir añadiendo parametros poniendole los nombres que quieras 


if __name__ == "__main__":
    app.run(debug=True)     # para poder ver los cambios de manera automática + loger.debug