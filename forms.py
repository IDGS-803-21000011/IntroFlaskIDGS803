from wtforms import Form
from wtforms import StringField, SelectField, RadioField, EmailField

class UserForm(Form):
    nombre = StringField('nombre')
    apaterno = StringField('apaterno')
    amaterno = StringField('amaterno')
    edad = StringField('edad')
    correo = StringField('correo')