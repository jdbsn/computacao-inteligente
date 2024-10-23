import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tqdm import tqdm
from utils.Funcoes import *
from alg_genetico.AlgoritmoGenetico import AlgoritmoGenetico
from utils.Boxplot import Boxplot
from utils.GraficoConvergencia import GraficoConvergencia

TAMANHO_POPULACAO = 30
GERACOES = 1000
DIMENSOES = 30
TAXA_CRUZAMENTO = 0.9
TAXA_MUTACAO = 0.01

boxplot = Boxplot()
convergencia = GraficoConvergencia()

cenarios = [
    (1, 1, "Roleta - 1 ponto de corte"),
    (1, 2, "Roleta - 2 pontos de corte"),
    (2, 1, "Torneio - 1 ponto de corte"), 
    (2, 2, "Torneio - 2 pontos de corte") 
]

def avaliar_sphere():
    for selecao, pontos_corte, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            algoritmo = AlgoritmoGenetico(TAMANHO_POPULACAO, GERACOES, DIMENSOES, TAXA_CRUZAMENTO, TAXA_MUTACAO, -100, 100, sphere)
            fitness = algoritmo.executar(selecao, pontos_corte)
            resultado_cenario.append(fitness)
            valores_convergencia.append(algoritmo.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Sphere - AG')
    convergencia.exibir_convergencia("Convengência da Função Sphere - AG")

def avaliar_rastrigin():
    for selecao, pontos_corte, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            algoritmo = AlgoritmoGenetico(TAMANHO_POPULACAO, GERACOES, DIMENSOES, TAXA_CRUZAMENTO, TAXA_MUTACAO, -30, 30, rastrigin)
            fitness = algoritmo.executar(selecao, pontos_corte)
            resultado_cenario.append(fitness)
            valores_convergencia.append(algoritmo.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Rastrigin - AG')
    convergencia.exibir_convergencia("Convengência da Função Rastrigin - AG")

def avaliar_rosenbrock():
    for selecao, pontos_corte, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao}'):
            algoritmo = AlgoritmoGenetico(TAMANHO_POPULACAO, GERACOES, DIMENSOES, TAXA_CRUZAMENTO, TAXA_MUTACAO, -5.12, 5.12, rosenbrock)
            fitness = algoritmo.executar(selecao, pontos_corte)
            resultado_cenario.append(fitness)
            valores_convergencia.append(algoritmo.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções da Função Rosenbrock - AG')
    convergencia.exibir_convergencia("Convengência da Função Rosenbrock - AG")


avaliar_rosenbrock()