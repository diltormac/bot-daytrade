from flask import Flask, render_template, request, redirect
from datetime import datetime
import random

app = Flask(__name__)

# Variáveis do bot
status_bot = "Aguardando..."
vitorias = 0
derrotas = 0
modo_operacao = "Normal"
nivel_martingale = 0
log_operacoes = []

@app.route("/", methods=["GET", "POST"])
def index():
    global status_bot, vitorias, derrotas, modo_operacao, nivel_martingale, log_operacoes

    if request.method == "POST":
        acao = request.form.get("acao")
        if acao == "iniciar":
            status_bot = "✅ Bot Iniciado"
        elif acao == "parar":
            status_bot = "⛔ Bot Parado"
        else:
            status_bot = "⚠️ Ação inválida"

        # Simula o resultado (para testes)
        if random.choice([True, False]):
            vitorias += 1
            nivel_martingale = 0
        else:
            derrotas += 1
            nivel_martingale += 1

        log_operacoes.append((datetime.now().strftime("%H:%M:%S"), status_bot))
        return redirect("/")

    return render_template("index.html",
                           status=status_bot,
                           wins=vitorias,
                           losses=derrotas,
                           modo=modo_operacao,
                           nivel=nivel_martingale,
                           log=log_operacoes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
