from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
log_operacoes = []

@app.route("/", methods=["GET", "POST"])
def index():
    global log_operacoes
    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "iniciar":
            resultado = "✅ Bot Iniciado"
        elif acao == "parar":
            resultado = "⛔ Bot Parado"
        else:
            resultado = "⚠️ Ação inválida"
        log_operacoes.append((datetime.now().strftime("%H:%M:%S"), resultado))
        return redirect("/")
    return render_template("index.html", log=log_operacoes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
