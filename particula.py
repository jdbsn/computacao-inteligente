class Particula:

    def __init__(self, posicao, velocidade, melhor_pos, melhor_fitness):
        self.posicao = posicao
        self.velocidade = velocidade
        self.melhor_pos = melhor_pos
        self.melhor_fitness = melhor_fitness

    def mover(self):
        for i in range(len(self.posicao)):
            self.posicao[i] += self.velocidade[i]