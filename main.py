from flask import Flask, render_template, request, redirect
from iqbot import IQBot
from datetime import datetime
import os

app = Flask(__name__)
bot = None
log_operacoes = []

@app.route("/", methods=["GET", "POST"])
def index():
    global bot

    if request.method == "POST":
        acao = request.form.get("acao")

        if acao == "iniciar":
            if not bot:
                email = os.getenv("IQ_EMAIL", "dilsontm@gmail.com")  # fallback
                senha = os.getenv("IQ_SENHA", "alana2011")
                bot = IQBot(email, senha)
                try:
                    saldo = bot.conectar()
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

    return render_template("index.html", log_operacoes=log_operacoes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
