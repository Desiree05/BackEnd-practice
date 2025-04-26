from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField, DecimalField
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductoForma(FlaskForm):
    nombre = StringField("Nombre", validators=[DataRequired()])
    cantidad = IntegerField("Cantidad", validators=[DataRequired()])
    precio = DecimalField("Precio", validators=[DataRequired()])
    categoria = StringField("Categoría", validators=[DataRequired()])
    guardar = SubmitField("Guardar")