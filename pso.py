import random
from particula import Particula
from funcoes import *

class Pso:

    inercia = 0.9 # w
    tipo_inecria = 1 # pode ser dentro da função
    inercia_max = 1
    inercia_min = 0.4
    coef_cognitivo = 2.05
    coef_social = 2.05
    qtd_iteracoes = 100
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

    def calcular_velocidade(self, particula):
        nova_velocidade = []

        for i in range(len(particula.velocidade)):
            i_pessoal = self.coef_cognitivo * random.uniform(0, 1) * (particula.melhor_pos[i] - particula.posicao[i])
            i_global = self.coef_cognitivo * random.uniform(0, 1) * (self.melhor_global[i] - particula.posicao[i])
            
            velocidade = self.inercia * particula.velocidade[i] + i_pessoal + i_global

            nova_velocidade.append(velocidade)

        return nova_velocidade


    def pso(self):
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
                novas_velocidades = self.calcular_velocidade(p)
                p.velocidade = novas_velocidades
                p.mover()

            # self.decaimento_linear(i)

            # print("---- Novas velocidades ----")
            # for i in self.populacao:
            #     print(i.velocidade)

pso = Pso()
pso.pso()