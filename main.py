from flask import Flask, render_template, request, redirect
from iqbot import IQBot
from datetime import datetime
import os

app = Flask(__name__)
bot = None
log_operacoes = []
saldo_atual = 0  # usado para manter o saldo visível mesmo após atualizações

@app.route("/", methods=["GET", "POST"])
def index():
    global bot, saldo_atual

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "iniciar":
            if not bot:
                bot = IQBot(os.environ.get("IQ_EMAIL"), os.environ.get("IQ_SENHA"))
                try:
                    saldo = bot.conectar()
                    saldo_atual = saldo  # atualiza o saldo global
                    resultado = f"✅ Bot conectado | Saldo demo: ${saldo:,.2f}"
                except Exception as e:
                    resultado = f"❌ Erro ao conectar: {str(e)}"
            else:
                resultado = "⚠️ Bot já está conectado."

        elif acao == "parar":
            if bot:
                bot.desconectar()
                bot = None
                resultado = "⛔ Bot desconectado"
            else:
                resultado = "⚠️ Bot já está desconectado."

        timestamp = datetime.now().strftime("%H:%M:%S")
        log_operacoes.insert(0, f"{timestamp} – {resultado}")

        return redirect("/")

    return render_template("index.html", log_operacoes=log_operacoes, saldo=f"{saldo_atual:,.2f}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
