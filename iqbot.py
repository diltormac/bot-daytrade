from iqoptionapi.stable_api import IQ_Option
import time

class IQBot:
    def __init__(self, email, senha):
        self.email = email
        self.senha = senha
        self.api = None

    def conectar(self):
        self.api = IQ_Option(self.email, self.senha)
        conectado, motivo = self.api.connect()

        if not conectado:
            raise Exception(f"Erro ao conectar: {motivo}")

        # Aguarda conexão
        while not self.api.check_connect():
            time.sleep(1)

        # Troca para conta prática
        self.api.change_balance("practice")

        # Aguarda o saldo atualizar
        time.sleep(1)

        saldo = self.api.get_balance()
        return saldo

    def desconectar(self):
        if self.api:
            self.api.close()
