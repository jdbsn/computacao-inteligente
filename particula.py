import random

class Particula:

    def __init__(self, posicao, velocidade, melhor_pos, melhor_fitness):
        self.posicao = posicao
        self.velocidade = velocidade
        self.melhor_pos = melhor_pos
        self.melhor_fitness = melhor_fitness

    def mover(self, limite_min, limite_max):
        for i in range(len(self.posicao)):
            nova_posicao = self.posicao[i] + self.velocidade[i]
            self.posicao[i] = min(max(nova_posicao, limite_min), limite_max)

    def calcular_velocidade(self, melhor_global, coef_cognitivo, coef_social, inercia):
        nova_velocidade = []

        for i in range(len(self.velocidade)):
            i_pessoal = coef_cognitivo * random.uniform(0, 1) * (self.melhor_pos[i] - self.posicao[i])
            i_global = coef_social * random.uniform(0, 1) * (melhor_global[i] - self.posicao[i])
            
            velocidade = inercia * self.velocidade[i] + i_pessoal + i_global

            nova_velocidade.append(velocidade)

        self.velocidade = nova_velocidade