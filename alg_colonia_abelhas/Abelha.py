import random


class Abelha:

    def __init__(self, posicao):
        self.posicao = posicao

    def mover(self, fonte_alimentacao, fonte_escolhida, limite_min, limite_max):
        indice = random.randint(0, len(self.posicao) - 1)
        valor = fonte_alimentacao[indice]

        novo_valor = valor + random.uniform(-1, 1) * (valor - fonte_escolhida[indice])
        self.posicao[indice] = min(max(novo_valor, limite_min), limite_max)
