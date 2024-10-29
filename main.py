from flask import Flask
import random

app = Flask(__name__)

datos = ["Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", "La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos"]

def gen_pass(pass_length):
    elements = "+-/*!&$#?=@<>ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    password = ""
    for i in range(pass_length):
        password += random.choice(elements)
    return password

@app.route("/")
def hello_world():
    return f'<h1>Bienvenido</h1><a href="/dato_aleatorio">Ver datos aleatorios</a><a href="/Contrasenna">Crear contraseña</a>'


@app.route("/dato_aleatorio")
def funcion_dato():
    return f'<p>{random.choice(datos)}</p>'

@app.route("/Contrasenna")
def contrasennas():
    return f'<p>{gen_pass(15)}</p>'

app.run(debug=True)