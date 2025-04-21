from flask import Flask, render_template, request, redirect
from datetime import datetime

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
        acao = request.form.get
