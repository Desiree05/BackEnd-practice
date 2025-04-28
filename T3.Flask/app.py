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

@app.route("/guardar", methods=["POST"])
def guardar():
    # Creamos los objetos de producto inicialmente objetos vacios
    producto = Producto()
    producto_forma = ProductoForma(obj=producto)

    if producto_forma.validate_on_submit():
        # Llenamos el objeto producto con los valores del formulario
        producto_forma.populate_obj(producto)   # también se pasa el id oculto, por lo que sabemos si estamos insertando uno nuevo o actualizando uno existente

        if not producto.id:
            # Si está vacio --> Guardamos el nuevo producto en la base de datos
            ProductoDAO.insertar(producto)
        else:
            ProductoDAO.actualizar(producto)
            
    # Redireccionamos a la página de inicio
    return redirect(url_for("inicio"))

@app.route("/limpiar")
def limpiar():
    return redirect(url_for("inicio"))

@app.route("/editar/<int:id>")
def editar(id):
    producto = ProductoDAO.seleccionar_por_id(id)
    producto_forma = ProductoForma(obj=producto)

    # Recuperar el listado de clientes para volver a mostrarlo
    productos_db = ProductoDAO.seleccionar()

    return render_template("index.html", titulo=titulo_app, productos=productos_db, forma=producto_forma)    


@app.route("/eliminar/<int:id>")
def eliminar(id):
    ProductoDAO.eliminar(id)
    return redirect(url_for("inicio"))


if __name__ == "__main__":
    app.run(debug=True)     # para poder ver los cambios de manera automática + loger.debug