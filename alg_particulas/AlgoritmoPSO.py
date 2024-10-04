import random

from tqdm import tqdm

from alg_particulas.Particula import Particula

class Pso:

    def __init__(self, coef_cognitivo, coef_social, inercia, qtd_iteracoes, qtd_particulas, funcao):
        self.coef_cognitivo = coef_cognitivo
        self.coef_social = coef_social
        self.inercia = inercia
        self.qtd_iteracoes = qtd_iteracoes
        self.qtd_particulas = qtd_particulas
        self.funcao = funcao
        self.melhor_global = []
        self.melhor_fitness = float('inf')
        self.populacao = []
        self.melhores_fitness = []
        self.limite_min = -100
        self.limite_max = 100
        self.dimensoes = 30
        self.inercia_max = 0.9
        self.inercia_min = 0.4
        
    def decaimento_linear(self, iteracao_atual):
        delta_inercia = self.inercia_max - self.inercia_min
        fator_progresso = (self.qtd_iteracoes - iteracao_atual) / self.qtd_iteracoes

        self.inercia = delta_inercia * fator_progresso + self.inercia_min

    def gerar_populacao(self, qtd_particulas, dimensoes, limite_min, limite_max, tipo_cooperacao):
        for _ in range(qtd_particulas):
            posicao = [random.randint(limite_min, limite_max) for _ in range(dimensoes)]
            velocidade = [random.uniform(limite_min * 0.2, limite_max * 0.2) for _ in range(dimensoes)]

            self.populacao.append(Particula(posicao, velocidade, posicao))

        if tipo_cooperacao == 1:
            for i in range(qtd_particulas):
                self.populacao[i].vizinho_esq = self.populacao[i - 1]
                self.populacao[i].vizinho_dir= self.populacao[(i + 1) % qtd_particulas]

    def avaliar_particula(self):
        for particula in self.populacao:
            fitness = self.funcao(particula.posicao)

            if fitness < particula.melhor_fitness:
                particula.melhor_fitness = fitness
                particula.melhor_pos = particula.posicao[:]

            if fitness < self.melhor_fitness:
                self.melhor_fitness = fitness
                self.melhor_global = particula.posicao[:]

    def executar(self, tipo_inercia, tipo_coop):
        self.gerar_populacao(self.qtd_particulas, self.dimensoes, self.limite_min, self.limite_max, tipo_coop)

        for i in tqdm(range(self.qtd_iteracoes), leave=False):
            self.avaliar_particula()
            
            self.melhores_fitness.append(self.melhor_fitness)

            # print("Iteração {} - Fitness: {}".format(i, self.melhor_fitness))

            for p in self.populacao:
                p.mover(self.limite_min, self.limite_max)
                p.calcular_velocidade(self.melhor_global, self.coef_cognitivo, self.coef_social, self.inercia, tipo_coop)

            if(tipo_inercia == 1):
                self.decaimento_linear(i)

        return self.melhor_fitness
