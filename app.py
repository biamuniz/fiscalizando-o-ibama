from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Olá, <b>mundo</b>!</p>"

@app.route("/sobre")
def sobre():
    return "<h1>Sobre</h1> <p>Esse site foi criado por <b>Bianca Muniz</b> como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do Insper.</p>"
