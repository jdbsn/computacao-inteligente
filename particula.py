import random

class Particula:

    def __init__(self, posicao, velocidade, melhor_pos, melhor_fitness):
        self.posicao = posicao
        self.velocidade = velocidade
        self.melhor_pos = melhor_pos
        self.melhor_fitness = melhor_fitness
        self.vizinho_esq = None
        self.vizinho_dir = None

    def mover(self, limite_min, limite_max):
        for i in range(len(self.posicao)):
            nova_posicao = self.posicao[i] + self.velocidade[i]
            self.posicao[i] = min(max(nova_posicao, limite_min), limite_max)

    def calcular_velocidade(self, melhor_global, coef_cognitivo, coef_social, inercia, tipo_coop):
        nova_velocidade = []

        if tipo_coop == 1:
            melhor_global = self.coop_local()

        for i in range(len(self.velocidade)):
            i_pessoal = coef_cognitivo * random.uniform(0, 1) * (self.melhor_pos[i] - self.posicao[i])
            i_global = coef_social * random.uniform(0, 1) * (melhor_global[i] - self.posicao[i])
            
            velocidade = inercia * self.velocidade[i] + i_pessoal + i_global

            nova_velocidade.append(velocidade)

        self.velocidade = nova_velocidade

    def coop_local(self):
        if self.vizinho_esq.melhor_fitness < self.melhor_fitness:
            return self.vizinho_esq.melhor_pos
        elif self.vizinho_dir.melhor_fitness < self.melhor_fitness:
            return self.vizinho_dir.melhor_pos
        else:
            return self.melhor_pos