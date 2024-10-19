import random
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


cenarios = [
    # (1, 2, "Roleta - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", sphere, -100, 100),
    (2, 2, "Torneio - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", rastrigin, -30, 30),
    # (1, 2, "Roleta - 2 pontos de corte (AG)", 1, 1, "Decaimento - Local (PSO)", rosenbrock, -5.12, 5.12) 
]

def avaliar_func():

    for selecao, pontos_corte, descricao_ag, tipo_inercia, tipo_coop, descricao_pso, funcao, limite_min, limite_max in cenarios:
        boxplot = Boxplot()
        convergencia = GraficoConvergencia()

        resultado_cenario = []
        valores_convergencia = []

        for _ in tqdm(range(20), desc=f'{descricao_ag}'):
            algoritmo = AlgoritmoGenetico(TAMANHO_POPULACAO, GERACOES, DIMENSOES, TAXA_CRUZAMENTO, 
                                          TAXA_MUTACAO, limite_min, limite_max, funcao)
            fitness = algoritmo.alg_genetico(selecao, pontos_corte)
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

        boxplot.exibir_boxplot('Boxplot de Execuções da Função Rastrigin - AG vs PSO')
        convergencia.exibir_convergencia("Convengência da Função Rastrigin - AG vs PSO")


# avaliar_func()

def colonia_abelhas():
    aca = AlgoritmoColoniaAbelhas(8, 10, 100, 1000, -100, 100, sphere)
    aca.gerar_fonte_alimentacao()

    print("Fonte Alimentação")
    for a in aca.fonte_alimentacao:
        print(a.posicao)

    print("Abelhas:")
    for a in aca.fonte_alimentacao:
        print(a.abelha.posicao)

    aca.mover_abelhas()

    print("Abelhas empregadas após mover:")
    for a in aca.fonte_alimentacao:
        print(a.abelha.posicao)
        
    for a in aca.fonte_alimentacao:
        a.verificar_posicao(sphere, a.abelha.posicao)

    print("Fonte Alimentação após verificar posição:")
    for a in aca.fonte_alimentacao:
        print(a.posicao, a.fator_abandono)

    print("Explorar fontes alimentações:")
    aca.explorar_fontes_alimentacoes()

    print("Fonte Alimentação após abelhas observadoras:")
    for a in aca.fonte_alimentacao:
        print(a.posicao, " | Fator abandono: ", a.fator_abandono)

colonia_abelhas()