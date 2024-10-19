class FonteAlimentacao:

    def __init__(self, valores, abelha):
        self.posicao = valores
        self.abelha = abelha
        self.fator_abandono = 0

    def verificar_posicao(self, funcao, posicao_abelha):
        fitness = funcao(self.posicao)
        fitness_abelha = funcao(posicao_abelha)

        if fitness_abelha < fitness:
            self.posicao = posicao_abelha
            self.fator_abandono = 0
        else:
            self.fator_abandono += 1
