import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tqdm import tqdm
from utils.Boxplot import Boxplot
from utils.GraficoConvergencia import GraficoConvergencia
from alg_particulas.AlgoritmoPSO import Pso
from utils.Funcoes import *

COEF_COGNITIVO = 2.05
COEF_SOCIAL = 2.05
INERCIA = 0.9
QTD_INTERACOES = 1000
QTD_PARTICULAS = 30

boxplot = Boxplot()
convergencia = GraficoConvergencia()

cenarios = [
    (0, 0, "Constante - Global"),
    (0, 1, "Constante - Local"),
    (1, 0, "Decaimento - Global"), 
    (1, 1, "Decaimento - Local") 
]

def avaliar_sphere():
    for tipo_inecria, tipo_coop, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES, QTD_PARTICULAS, sphere, -100, 100)
            fitness = pso.executar(tipo_inecria, tipo_coop)
            resultado_cenario.append(fitness)
            valores_convergencia.append(pso.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Sphere - PSO')
    convergencia.exibir_convergencia("Convergência da Função Sphere - PSO")

def avaliar_rastrigin():
    for tipo_inecria, tipo_coop, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES, QTD_PARTICULAS, rastrigin, -30, 30)
            fitness = pso.executar(tipo_inecria, tipo_coop)
            resultado_cenario.append(fitness)
            valores_convergencia.append(pso.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Rastrigin - PSO')
    convergencia.exibir_convergencia("Convergência da Função Rastrigin - PSO")

def avaliar_rosenbrock():
    for tipo_inecria, tipo_coop, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES, QTD_PARTICULAS, rosenbrock, -5.12, 5.12)
            fitness = pso.executar(tipo_inecria, tipo_coop)
            resultado_cenario.append(fitness)
            valores_convergencia.append(pso.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Rosenbrock - PSO')
    convergencia.exibir_convergencia("Convergência da Função Rosenbrock - PSO")


avaliar_rosenbrock()