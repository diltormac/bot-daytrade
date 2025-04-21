from iqoptionapi.stable_api import IQ_Option
import time

class IQBot:
    def __init__(self, email, senha):
        self.api = IQ_Option(email, senha)

    def conectar(self):
        conectado, motivo = self.api.connect()
        if not conectado:
            raise Exception(motivo)

        while not self.api.check_connect():
            time.sleep(1)

        self.api.change_balance("practice")
        time.sleep(1)
        return self.api.get_balance()

    def desconectar(self):
        if self.api:
            self.api.close()
