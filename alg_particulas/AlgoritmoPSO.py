import random

from tqdm import tqdm

from alg_particulas.Particula import Particula
from utils.Funcoes import *

class Pso:

    def __init__(self, coef_cognitivo, coef_social, inercia, qtd_iteracoes):
        self.coef_cognitivo = coef_cognitivo
        self.coef_social = coef_social
        self.inercia = inercia
        self.qtd_iteracoes = qtd_iteracoes
        self.melhor_global = []
        self.melhor_fitness = float('inf')
        self.populacao = []
        self.limite_min = -100
        self.limite_max = 100
        self.dimensoes = 30
        self.inercia_max = 1
        self.inercia_min = 0.4
        self.qtd_particulas = 30
        self.melhores_fitness = []

    def decaimento_linear(self, iteracao_atual):
        self.inercia = (self.inercia_max - self.inercia_min) * ((self.qtd_iteracoes - iteracao_atual) / self.qtd_iteracoes) + self.inercia_min

    def gerar_populacao(self, qtd_particulas, dimensoes, limite_min, limite_max, tipo_cooperacao):
        for _ in range(qtd_particulas):
            posicao = [random.randint(limite_min, limite_max) for _ in range(dimensoes)]
            velocidade = [random.randint(limite_min * 0.2, limite_max * 0.2) for _ in range(dimensoes)]

            self.populacao.append(Particula(posicao, velocidade, posicao, None))

        if tipo_cooperacao == 1:
            for i in range(qtd_particulas):
                self.populacao[i].vizinho_esq = self.populacao[i - 1]
                self.populacao[i].vizinho_dir= self.populacao[(i + 1) % qtd_particulas]

    def avaliar_particula(self):
        for particula in self.populacao:
            fitness = sphere(particula.posicao)

            if(particula.melhor_fitness is None or fitness < particula.melhor_fitness):
                particula.melhor_fitness = fitness
                particula.melhor_pos = particula.posicao[:]

            if(self.melhor_fitness is None or fitness < self.melhor_fitness):
                self.melhor_fitness = fitness
                self.melhor_global = particula.posicao[:]

    def executar(self, tipo_inecria, tipo_coop):
        self.gerar_populacao(self.qtd_particulas, self.dimensoes, self.limite_min, self.limite_max, tipo_coop)

        for i in tqdm(range(self.qtd_iteracoes)):
            self.avaliar_particula()
            
            self.melhores_fitness.append(self.melhor_fitness)

            # print("Iteração {} - Fitness: {}".format(i, self.melhor_fitness))

            for p in self.populacao:
                p.mover(self.limite_min, self.limite_max)
                p.calcular_velocidade(self.melhor_global, self.coef_cognitivo, self.coef_social, self.inercia, tipo_coop)

            if(tipo_inecria == 1):
                self.decaimento_linear(i)

        return self.melhor_fitness
