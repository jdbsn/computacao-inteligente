import random

from alg_colonia_abelhas.FonteAlimentacao import FonteAlimentacao
from alg_colonia_abelhas.Abelha import Abelha
from utils.Funcoes import *


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
            abelha = Abelha(posicoes.copy())
            self.fonte_alimentacao.append(FonteAlimentacao(posicoes, abelha))
