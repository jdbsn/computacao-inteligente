from tqdm import tqdm

from alg_colonia_abelhas.AlgoritmoColoniaAbelhas import AlgoritmoColoniaAbelhas
from alg_genetico.AlgoritmoGenetico import AlgoritmoGenetico
from alg_particulas.AlgoritmoPSO import Pso
from utils.Boxplot import Boxplot
from utils.Funcoes import *
from utils.GraficoConvergencia import GraficoConvergencia


COEF_COGNITIVO = 2.05
COEF_SOCIAL = 2.05
INERCIA = 0.9
QTD_INTERACOES = 1000
QTD_PARTICULAS = 30

TAMANHO_POPULACAO = 30
GERACOES = 1000
DIMENSOES = 30
TAXA_CRUZAMENTO = 0.9
TAXA_MUTACAO = 0.01

funcs = [
    # (sphere, -100, 100), 
    # (rastrigin, -30, 30), 
    (rosenbrock, -5.12, 5.12)
]

boxplot = Boxplot()
convergencia = GraficoConvergencia()

def avaliar_func():
    cenarios = [
        # (1, 2, "Roleta - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", 100, "Critério de abandono: 100 (ABC)"),
        (2, 2, "Torneio - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", 100, "Critério de abandono: 100 (ABC)"),
    #     (1, 2, "Roleta - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", 100, "Critério de abandono: 100 (ABC)") 
    ]

    for funcao, limite_min, limite_max in funcs:
        for selecao, pontos_corte, descricao_ag, tipo_inercia, tipo_coop, descricao_pso, criterio_abandono, descricao_abc in cenarios:
            resultado_cenario = []
            valores_convergencia = []

            for _ in tqdm(range(20), desc=f'{descricao_ag}'):
                algoritmo = AlgoritmoGenetico(TAMANHO_POPULACAO, GERACOES, DIMENSOES, TAXA_CRUZAMENTO, 
                                            TAXA_MUTACAO, limite_min, limite_max, funcao)
                fitness = algoritmo.executar(selecao, pontos_corte)
                resultado_cenario.append(fitness)
                valores_convergencia.append(algoritmo.melhores_fitness)

            boxplot.adicionar_dados(resultado_cenario)
            media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
            print(media[-1])
            convergencia.adicionar_dados(media, descricao_ag)
            print()
            
            resultado_cenario = []
            valores_convergencia = []

            for _ in tqdm(range(20), desc=f'{descricao_pso}'):
                pso = Pso(COEF_COGNITIVO, COEF_SOCIAL, INERCIA, QTD_INTERACOES, QTD_PARTICULAS, 
                        funcao, limite_min, limite_max)
                fitness = pso.executar(tipo_inercia, tipo_coop)
                resultado_cenario.append(fitness)
                valores_convergencia.append(pso.melhores_fitness)

            boxplot.adicionar_dados(resultado_cenario)
            media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
            print(media[-1])
            convergencia.adicionar_dados(media, descricao_pso)
            print()

            resultado_cenario = []
            valores_convergencia = []

            for _ in tqdm(range(20), desc=f'{descricao_abc}'):
                algoritmo = AlgoritmoColoniaAbelhas(TAMANHO_POPULACAO, DIMENSOES, QTD_INTERACOES, 
                                                    limite_min, limite_max, funcao)

                fitness = algoritmo.executar(criterio_abandono)
                resultado_cenario.append(fitness)
                valores_convergencia.append(algoritmo.melhores_fitness)

            boxplot.adicionar_dados(resultado_cenario)
            media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
            print(media[-1])
            convergencia.adicionar_dados(media, descricao_abc)
            print()

            boxplot.exibir_boxplot(f'Boxplot de Execuções da Função {funcao.__name__.capitalize()} - AG vs PSO vs ABC')
            convergencia.exibir_convergencia(f'Convengência da Função {funcao.__name__.capitalize()} - AG vs PSO vs ABC')

            boxplot.resetar()
            convergencia.resetar()

avaliar_func()

def colonia_abelhas():
    cenarios = [
        # (10, "Critério de abandono: 10 (ABC)"),
        # (50, "Critério de abandono: 50 (ABC)"),
        (100, "Critério de abandono: 100 (ABC)") 
    ]

    for funcao, limite_min, limite_max in funcs:
        for criterio_abandono, descricao in cenarios:
            resultado_cenario = []
            valores_convergencia = []

            for _ in tqdm(range(1), desc=f'{descricao}'):
                algoritmo = AlgoritmoColoniaAbelhas(TAMANHO_POPULACAO, DIMENSOES, 100000, 
                                                    limite_min, limite_max, funcao)

                fitness = algoritmo.executar(criterio_abandono)
                resultado_cenario.append(fitness)
                valores_convergencia.append(algoritmo.melhores_fitness)

            boxplot.adicionar_dados(resultado_cenario)
            media = [sum(elementos) / len(elementos) for elementos in zip(*valores_convergencia)]
            print(media[-1])
            convergencia.adicionar_dados(media, descricao)
            print()
                
        boxplot.exibir_boxplot(f'Boxplot de Execuções da Função {funcao.__name__.capitalize()} - ABC')
        convergencia.exibir_convergencia(f"Convengência da Função {funcao.__name__.capitalize()} - ABC")

        boxplot.resetar()
        convergencia.resetar()

# colonia_abelhas()