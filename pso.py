import random
from particula import Particula
from funcoes import *

class Pso:

    inercia = 0.9 # w
    inercia_max = 1
    inercia_min = 0.4
    coef_cognitivo = 2.05
    coef_social = 2.05
    qtd_iteracoes = 1000
    qtd_particulas = 10
    melhor_global = []
    melhor_fitness = None
    populacao = []

    def decaimento_linear(self, iteracao_atual):
        self.inercia = (self.inercia_max - self.inercia_min) * ((self.qtd_iteracoes - iteracao_atual) / self.qtd_iteracoes) + self.inercia_min


    def gerar_populacao(self, qtd_particulas, dimensoes, limite_min, limite_max):
        for _ in range(qtd_particulas):
            posicao = [random.randint(limite_min, limite_max) for _ in range(dimensoes)]
            velocidade = [random.randint(limite_min, limite_max) for _ in range(dimensoes)]

            self.populacao.append(Particula(posicao, velocidade, posicao, None))

    def avaliar_particula(self):
        
        for particula in self.populacao:
            fitness = sphere(particula.posicao)

            if(particula.melhor_fitness is None or fitness < particula.melhor_fitness):
                particula.melhor_fitness = fitness
                particula.melhor_pos = particula.posicao[:]

            if(self.melhor_fitness is None or fitness < self.melhor_fitness):
                self.melhor_fitness = fitness
                self.melhor_global = particula.posicao[:]

    def pso(self, tipo_inecria = 0):
        self.gerar_populacao(self.qtd_particulas, 2, 0, 100)

        for i in self.populacao:
            print(i.posicao)

        for i in range(self.qtd_iteracoes):

            self.avaliar_particula()

            # print("---- Velocidades ----")
            # for i in self.populacao:
            #     print(i.posicao)

            print("---- Melhor global ----")
            print(self.melhor_fitness)
            print(self.melhor_global)

            for p in self.populacao:
                p.calcular_velocidade(self.melhor_global, self.coef_cognitivo, self.coef_social, self.inercia)
                p.mover()

            if(tipo_inecria == 1):
                self.decaimento_linear(i)

            # print("---- Novas velocidades ----")
            # for i in self.populacao:
            #     print(i.velocidade)

pso = Pso()

print("Selecione o fator de inércia: \n 0 - Constante (padrão) | 1 - Decaimento linear")
tipo_inecria = int(input())

pso.pso(tipo_inecria)