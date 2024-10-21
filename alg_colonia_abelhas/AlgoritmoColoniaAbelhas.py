import random

from alg_colonia_abelhas.FonteAlimentacao import FonteAlimentacao
from alg_colonia_abelhas.Abelha import Abelha
from alg_genetico.EstrategiaSelecao import EstrategiaSelecao
from utils.Funcoes import *


class AlgoritmoColoniaAbelhas:
    
    def __init__(self, tamanho_populacao, dimensoes, ciclos, limite_min, limite_max, funcao):
        self.tamanho_populacao = tamanho_populacao
        self.dimensoes = dimensoes
        self.ciclos = ciclos
        self.limite_min = limite_min
        self.limite_max = limite_max
        self.funcao = funcao
        self.fonte_alimentacao = []
        self.melhor_resultado = []
        self.melhor_fitness = float('inf')
        self.melhores_fitness = []

    def gerar_fonte_alimentacao(self):
        for _ in range(self.tamanho_populacao//2):
            posicoes = [random.uniform(self.limite_min, self.limite_max) for _ in range(self.dimensoes)]
            abelha = Abelha(posicoes.copy())
            self.fonte_alimentacao.append(FonteAlimentacao(posicoes, abelha))

    def mover_abelhas(self):
        for i in range(len(self.fonte_alimentacao)):
            abelha = self.fonte_alimentacao[i].abelha

            indice = i
            while indice == i:
                indice = random.randint(0, len(self.fonte_alimentacao) - 1)

            abelha.mover(self.fonte_alimentacao[indice].posicao)

    def explorar_fontes_alimentacoes(self):
        lista_fitness = []

        for fonte in self.fonte_alimentacao:
            fitness = self.funcao(fonte.posicao)
            lista_fitness.append(fitness)

        fontes_selecionadas = EstrategiaSelecao.f_fitnes(self.fonte_alimentacao, self.tamanho_populacao//2, lista_fitness, True)

        for i in range(len(fontes_selecionadas)):
            abelha_observadora = Abelha(fontes_selecionadas[i].posicao.copy())
            abelha_observadora.mover(fontes_selecionadas[i].posicao.copy())
            fontes_selecionadas[i].verificar_posicao(self.funcao, abelha_observadora.posicao)

    def executar(self, criterio_abandono):
        self.gerar_fonte_alimentacao()
        
        for _ in range(self.ciclos):
            self.mover_abelhas()
        
            for fonte in self.fonte_alimentacao:
                fonte.verificar_posicao(self.funcao, fonte.abelha.posicao)

            self.explorar_fontes_alimentacoes()

            for fonte in self.fonte_alimentacao:
                if fonte.fator_abandono > criterio_abandono:
                    posicao = [random.uniform(self.limite_min, self.limite_max) for _ in range(self.dimensoes)]
                    fonte.posicao = posicao	
                    fonte.fator_abandono = 0
                    fonte.abelha.posicao = fonte.posicao
            
            lista_fitness = []
            for fonte in self.fonte_alimentacao:
                fitness = self.funcao(fonte.posicao)
                lista_fitness.append(fitness)

            menor_fitness = min(lista_fitness)
            self.melhores_fitness.append(menor_fitness)

            if self.melhor_fitness > menor_fitness:
                self.melhor_fitness = menor_fitness
                self.melhor_resultado = self.fonte_alimentacao[lista_fitness.index(menor_fitness)].posicao