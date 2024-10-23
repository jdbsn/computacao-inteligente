import random

from tqdm import tqdm

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

    def mover_abelha(self, posicao_fonte, abelha, indice):
        indice_selecionado = indice
        while indice_selecionado == indice:
            indice = random.randint(0, len(posicao_fonte) - 1)

        abelha.mover(posicao_fonte, self.fonte_alimentacao[indice_selecionado].posicao, 
                         self.limite_min, self.limite_max)

    def explorar_fontes_alimentacoes(self):
        lista_fitness = [self.funcao(fonte.posicao) for fonte in self.fonte_alimentacao]

        fontes_selecionadas = EstrategiaSelecao.f_fitnes(self.fonte_alimentacao, self.tamanho_populacao//2, 
                                                         lista_fitness, True)

        for i in range(len(fontes_selecionadas)):
            abelha_observadora = Abelha(fontes_selecionadas[i].posicao.copy())

            self.mover_abelha(fontes_selecionadas[i].posicao, abelha_observadora, i)
            fontes_selecionadas[i].verificar_posicao(self.funcao, abelha_observadora.posicao.copy())

    def verificar_fator_abandono(self, criterio_abandono):
        for fonte in self.fonte_alimentacao:
            if fonte.fator_abandono > criterio_abandono:
                posicao = [random.uniform(self.limite_min, self.limite_max) for _ in range(self.dimensoes)]
                fonte.posicao = posicao	
                fonte.fator_abandono = 0
                fonte.abelha.posicao = fonte.posicao.copy()

    def executar(self, criterio_abandono):
        self.gerar_fonte_alimentacao()

        for _ in tqdm(range(self.ciclos), leave=False):
            for i in range(len(self.fonte_alimentacao)):
                fonte_alimentacao = self.fonte_alimentacao[i]
                self.mover_abelha(fonte_alimentacao.posicao, fonte_alimentacao.abelha, i)
                fonte_alimentacao.verificar_posicao(self.funcao, fonte_alimentacao.abelha.posicao)
                
            self.explorar_fontes_alimentacoes()
            self.verificar_fator_abandono(criterio_abandono)

            lista_fitness = [self.funcao(fonte.posicao) for fonte in self.fonte_alimentacao]
            menor_fitness = min(lista_fitness)
            
            if self.melhor_fitness > menor_fitness:
                self.melhor_fitness = menor_fitness
                self.melhor_resultado = self.fonte_alimentacao[lista_fitness.index(menor_fitness)].posicao
            
            self.melhores_fitness.append(self.melhor_fitness)

        return self.melhor_fitness