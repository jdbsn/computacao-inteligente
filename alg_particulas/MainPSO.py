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
QTD_INTERACOES = 4000
QTD_PARTICULAS = 30

boxplot = Boxplot()
convergencia = GraficoConvergencia()

def avaliar_sphere():
    cenarios = [
        (0, 0, "Constante - Global"),
        (0, 1, "Constante - Local"),
        (1, 0, "Decaimento - Global"), 
        (1, 1, "Decaimento - Local") 
    ]

    for tipo_inecria, tipo_coop, descricao in cenarios:
        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(4), desc=f'{descricao}'):
            pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES, QTD_PARTICULAS, sphere)
            fitness = pso.executar(tipo_inecria, tipo_coop)
            resultado_cenario.append(fitness)
            valores_convergencia.append(pso.melhores_fitness)

        boxplot.adicionar_dados(resultado_cenario)
        media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
        print(media[-1])
        convergencia.adicionar_dados(media, descricao)
        print()

    boxplot.exibir_boxplot('Boxplot de Execuções em Diferentes Cenários - PSO')

    convergencia.exibir_convergencia("Convergência da Função Sphere - PSO")

 
avaliar_sphere()