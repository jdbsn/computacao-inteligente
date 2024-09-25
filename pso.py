import random

from boxplot import Boxplot
from particula import Particula
from funcoes import *

class Pso:

    inercia = 0.9 # w
    inercia_max = 1
    inercia_min = 0.4
    coef_cognitivo = 2.05
    coef_social = 2.05
    qtd_iteracoes = 2
    qtd_particulas = 10
    melhor_global = []
    melhor_fitness = None
    populacao = []
    dimensoes = 50
    limite_min = -10
    limite_max = 10

    def decaimento_linear(self, iteracao_atual):
        self.inercia = (self.inercia_max - self.inercia_min) * ((self.qtd_iteracoes - iteracao_atual) / self.qtd_iteracoes) + self.inercia_min

    def gerar_populacao(self, qtd_particulas, dimensoes, limite_min, limite_max):
        for _ in range(qtd_particulas):
            posicao = [random.randint(limite_min, limite_max) for _ in range(dimensoes)]
            velocidade = [random.randint(limite_min * 0.2, limite_max * 0.2) for _ in range(dimensoes)]

            self.populacao.append(Particula(posicao, velocidade, posicao, None))

    def avaliar_particula(self):
        fitness_iteracao = []

        for particula in self.populacao:
            fitness = sphere(particula.posicao)
            fitness_iteracao.append(fitness)

            if(particula.melhor_fitness is None or fitness < particula.melhor_fitness):
                particula.melhor_fitness = fitness
                particula.melhor_pos = particula.posicao[:]

            if(self.melhor_fitness is None or fitness < self.melhor_fitness):
                self.melhor_fitness = fitness
                self.melhor_global = particula.posicao[:]

        return fitness_iteracao

    def pso(self, tipo_inecria = 0):
        self.gerar_populacao(self.qtd_particulas, self.dimensoes, self.limite_min, self.limite_max)

        for i in self.populacao:
            print(i.posicao, end=" ")

        print()

        for i in range(self.qtd_iteracoes):

            fitness_iteracao = self.avaliar_particula()
            boxplot.adicionar_dados(fitness_iteracao)

            print("Iteração {} - Fitness: {}".format(i, self.melhor_fitness))

            for p in self.populacao:
                p.calcular_velocidade(self.melhor_global, self.coef_cognitivo, self.coef_social, self.inercia)
                p.mover(self.limite_min, self.limite_max)

            if(tipo_inecria == 1):
                self.decaimento_linear(i)


pso = Pso()
boxplot = Boxplot()

print("Selecione o fator de inércia: \n 0 - Constante (padrão) | 1 - Decaimento linear")
tipo_inecria = int(input())

pso.pso(tipo_inecria)
boxplot.exibir_boxplot()