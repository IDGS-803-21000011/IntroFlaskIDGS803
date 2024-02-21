from flask import Flask, render_template, request, flash, Response, g, redirect
from flask_wtf.csrf import CSRFProtect
import forms

app = Flask(__name__)
app.secret_key = 'Esta es la clave secreta'

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# -----------------
@app.before_request
def before_request():
    #g.nombre = "Daniel"
    print("before_request")

@app.after_request
def after_request(response):
    print("ultimo")
    # if 'Daniel' not in g.nombre and request.endpoint not in ['/index']:
    #     return redirect('index.html')
    return response
# -----------

@app.route("/index")
def index():
    g.nombre = "Daniel"
    escuela = "UTL!!!"
    alumnos = ["Gael", "Pedro", "Alicia", "Ana"]
    return render_template("index.html", escuela = escuela, alumnos = alumnos)

@app.route("/alumnos", methods=["GET", "POST"])
def alumn():
    print("Hola alumnos")
    #print("Hola: {}".format(g.nombre))
    nom = ''
    apa = ''
    ama = ''
    alum_form = forms.UserForm(request.form)
    if request.method == "POST" and alum_form.validate():
        nom = alum_form.nombre.data
        apa = alum_form.apaterno.data
        ama = alum_form.amaterno.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)
        print("Nombre: {}".format(nom))
        print("apaterno: {}".format(apa))
        print("amaterno: {}".format(ama))
    return render_template("alumnos.html", form = alum_form, nom=nom, apa=apa, ama=ama)

@app.route("/maestros")
def maestr():
    return render_template("maestros.html")



@app.route("/hola")
def hola():
    return "<p><h1>Hola desde HOLA!!!<br> Mundo</br></h1></p>"

@app.route("/user/<string:name>")
def user(name):
    return "<h1>Hola " + name + "</h1>"

@app.route("/numero/<int:n>")
def numero(n):
    return "El numero es: {}".format(n)

@app.route("/user/<int:id>/<string:name>")
def func(id, name):
    return "ID: {} Nombre: {}".format(id, name)

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return "La suma de {} + {} es: {}".format(n1, n2, n1 + n2)

@app.route("/default")
@app.route("/default/<string:ab>")
def func1(ab = "UTL"):
    return "El valor es " + ab

@app.route("/multiplicar", methods=["GET", "POST"])
def mult():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")

        return "<h1>La multiplicacion es: {}</h1>".format(str(int(num1) * int(num2)))
    else:
        return '''
        <form action="/multiplicar" method="POST">
            <label>N1: </label>
            <input type="text" name="n1"/><br>
            <label>N2: </label>
            <input type="text" name="n2"/><br>
            <button type="subbmit">Calcular</button>
        </form>
        '''

@app.route("/formulario1")
def formulario():
    return render_template("formulario1.html")

@app.route("/formulario2")
def formulario2():
    return render_template("formulario2.html")

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    if request.method == "POST":
        num1=request.form.get("n1")
        num2=request.form.get("n2")
        return "<h1>La multiplicacion es: {}</h1>".format(str(int(num1) * int(num2)))

if __name__ == "__main__":
    app.run(debug=True)
