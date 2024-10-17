import random

from FonteAlimentacao import FonteAlimentacao
from Abelha import Abelha

tamanho = 0

class AlgoritmoColoniaAbelhas:
    
    def __init__(self, tamanho_populacao, dimensoes, criterio_abandono, ciclos, limite_min, limite_max):
        self.tamanho_populacao = tamanho_populacao
        self.dimensoes = dimensoes
        self.criterio_abandono = criterio_abandono
        self.ciclos = ciclos
        self.limite_min = limite_min
        self.limite_max = limite_max
        self.fonte_alimentacao = []

    def gerar_fonte_alimentacao(self):
        for _ in range(self.tamanho_populacao//2):
            posicoes = [random.randint(self.limite_min, self.limite_max) for _ in range(self.dimensoes)]
            abelha = Abelha(posicoes)
            self.fonte_alimentacao.append(FonteAlimentacao(posicoes, abelha))

aca = AlgoritmoColoniaAbelhas(4, 2, 100, 1000, -100, 100)
aca.gerar_fonte_alimentacao()

for a in aca.fonte_alimentacao:
    print(a.posicao)

for a in aca.fonte_alimentacao:
    print(a.abelha.posicao)
