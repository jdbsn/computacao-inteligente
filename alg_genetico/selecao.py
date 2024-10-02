import random

class Selecao:
    
    @staticmethod
    def f_fitnes(populacao, tamanho_populacao, fitness):
        total_fitness = sum(fitness)
        probabilidades = []

        for valor in fitness:
            probabilidades.append(valor/total_fitness)

        selecionados = []
        for _ in range(tamanho_populacao):
            cromossomo_selecionado = Selecao.roleta(populacao, probabilidades)
            
            selecionados.append(cromossomo_selecionado)

        return selecionados

    def roleta(cromossomo, probabilidades):
        somar = 0
        acumulado = []
        for valor in probabilidades:
            somar += valor
            acumulado.append(somar)

        sorteio = random.uniform(0, 1)

        for i, limite in enumerate(acumulado):
            if sorteio >= limite:
                return cromossomo[i]

    @staticmethod        
    def torneio(populacao, fitness):
        resultado = []

        for _ in populacao:
            indice1 = random.randint(0, len(populacao)-1)
            indice2 = random.randint(0, len(populacao)-1)

            valor1 = fitness[indice1]
            valor2 = fitness[indice2]

            if valor1 < valor2:
                resultado.append(populacao[indice1])
            else:
                resultado.append(populacao[indice2])

        return resultado	