import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tqdm import tqdm
from utils.Boxplot import Boxplot
from utils.GraficoConvergencia import GraficoConvergencia
from alg_particulas.AlgoritmoPSO import Pso


def main():
    # print("Selecione o fator de inércia: \n 0 - Constante | 1 - Decaimento linear")
    # tipo_inecria = int(input())

    # print("Selecione o tipo de: \n 0 - Global | 1 - Local")
    # tipo_coop = int(input())

    COEF_COGNITIVO = 2.05
    COEF_SOCIAL = 2.05
    INERCIA = 0.9
    QTD_INTERACOES = 4000

    cenarios = [
        (0, 0, "Constante - Global"),
        (0, 1, "Constante - Local"),
        (1, 0, "Decaimento - Global"), 
        (1, 1, "Decaimento - Local") 
    ]

    boxplot = Boxplot()
    convergencia = GraficoConvergencia()

    for tipo_inecria, tipo_coop, descricao in cenarios:
        resultado_cenario = []

        for _ in tqdm(range(1), desc=f'{descricao}'):
            pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES)
            fitness = pso.executar(tipo_inecria, tipo_coop)
            resultado_cenario.append(fitness)
            convergencia.adicionar_dados(pso.melhores_fitness, descricao)

        boxplot.adicionar_dados(resultado_cenario)
        print()

    boxplot.exibir_boxplot()


    # convergencia.exibir_convergencia()

 
main()