from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    jogos = [
        {"nome": "Adivinhe o número", "rota": "adivinhe"},
        {"nome": "Batalha Naval", "rota": "batalha_naval"},
        {"nome": "Forca", "rota": "forca"},
        {"nome": "Pedra, Papel e Tesoura", "rota": "pedra_papel_tesoura"},
        {"nome": "Quiz Geek", "rota": "quiz"},
        {"nome": "Torre de Hanói", "rota": "torre_hanoi"}
    ]
    return render_template("index.html", jogos=jogos)


@app.route("/adivinhe", methods=["GET", "POST"])
def adivinhe():
    if request.method == "POST":
        pass
    return render_template("adivinhe.html")


@app.route("/batalha_naval", methods=["GET", "POST"])
def batalha_naval():
    if request.method == "POST":
        pass
    return render_template("batalha_naval.html")


@app.route("/forca", methods=["GET", "POST"])
def forca():
    if request.method == "POST":
        pass
    return render_template("forca.html")


@app.route("/pedra_papel_tesoura", methods=["GET", "POST"])
def pedra_papel_tesoura():
    if request.method == "POST":
        # lógica do jogo
        pass
    return render_template("pedra_papel_tesoura.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    if request.method == "POST":
        pass
    return render_template("quiz.html")


@app.route("/torre_hanoi", methods=["GET", "POST"])
def torre_hanoi():
    if request.method == "POST":
        pass
    return render_template("torre_hanoi.html")


if __name__ == "__main__":
    app.run(debug=True)
