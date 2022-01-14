from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
        <h1>Fiscalizando o Ibama</h1>
        <a href="/sobre">Sobre esse site</a>
        <p>
            Visualizando a quantidade de multas ambientais aplicadas no âmbito do Ibama que estão em <b>homologação ou prazo de defesa</b> nos estados que integram o território da Amazônia Legal.
        </p>
    """

@app.route("/sobre")
def sobre():
    return """
        <h1>Sobre</h1>
        <a href="/">Página inicial</a>
        <p>
            Esse site foi criado por <b>Bianca Muniz</b> como projeto final para obtenção da certificação em Jornalismo de Dados e Automação do Insper.
        </p>
            """
