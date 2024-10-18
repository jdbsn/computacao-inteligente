import random


class Abelha:

    def __init__(self, posicao):
        self.posicao = posicao

    def mover(self, fonte_alimentacao):
        indice = random.randint(0, len(self.posicao) - 1)
        valor = self.posicao[indice]

        novo_valor = valor + random.uniform(-1, 1) * (valor - fonte_alimentacao[indice])
        self.posicao[indice] = novo_valor
        