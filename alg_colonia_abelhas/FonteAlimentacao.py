class FonteAlimentacao:

    def __init__(self, valores, abelha):
        self.posicao = valores
        self.abelha = abelha
        self.fator_abandono = 0

    def verificar_posicao(self, funcao):
        fitness = funcao(self.posicao)
        fitness_abelha = funcao(self.abelha.posicao)

        if fitness_abelha < fitness:
            self.posicao = self.abelha.posicao
            self.fator_abandono = 0
        else:
            self.fator_abandono += 1
