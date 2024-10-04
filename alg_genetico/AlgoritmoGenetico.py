import random
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tqdm import tqdm
from alg_genetico.EstrategiaSelecao import EstrategiaSelecao
from utils.Funcoes import *

class AlgoritmoGenetico:

    def __init__(self, tamanho_populacao, geracoes, dimensoes, taxa_cruzamento, taxa_mutacao, min_gene, max_gene,):
        self.tamanho_populacao = tamanho_populacao
        self.geracoes = geracoes
        self.dimensoes = dimensoes
        self.taxa_cruzamento = taxa_cruzamento
        self.taxa_mutacao = taxa_mutacao
        self.min_gene = min_gene
        self.max_gene = max_gene
        self.melhores_fitness = []

    def gerar_populacao(self):
        populacao = []

        for _ in range(self.tamanho_populacao):
            cromossomo = []
            for _ in range(self.dimensoes):    
                cromossomo.append(random.uniform(self.min_gene, self.max_gene))
            populacao.append(cromossomo)

        return populacao

    def cruzamento(self, pais, pontos = 1):
        resultado = []

        if len(pais) % 2 != 0:
            pais.pop(random.randint(0, len(pais)-1))

        for i in range(0, len(pais), 2):
            valor = random.uniform(0, 1)
            
            if(valor > self.taxa_cruzamento):
                resultado += pais[i:i+2]  
            else:
                if pontos > self.dimensoes - 1:
                    pontos = self.dimensoes - 1
                
                pontos_corte = sorted(random.sample(range(1, self.dimensoes-1), pontos))

                pai1 = pais[i]
                pai2 = pais[i+1]

                filho1 = []
                filho2 = []
                aux = 0

                for i in range(0, len(pontos_corte)):
                    if(i % 2 == 0):
                        filho1 += pai1[aux:pontos_corte[i]]
                        filho2 += pai2[aux:pontos_corte[i]]
                    else:
                        filho1 += pai2[aux:pontos_corte[i]]
                        filho2 += pai1[aux:pontos_corte[i]]
                    aux = pontos_corte[i]

                filho1 += pai1[aux:]
                filho2 += pai2[aux:]

                resultado.extend([filho1, filho2])

        return resultado

    def mutacao(self, populacao):
        for cromossomo in populacao:
            for i in range(len(cromossomo)):
                    valor = random.uniform(0, 1)
                    if valor <= self.taxa_mutacao:
                        cromossomo[i] = random.uniform(self.min_gene, self.max_gene)

        return populacao

    def alg_genetico(self, forma_selecao, pontos):
        populacao = self.gerar_populacao()
        fitness = []

        for _ in tqdm(range(self.geracoes), leave=False):
            fitness = [sphere(cromossomo) for cromossomo in populacao]

            self.melhores_fitness.append(min(fitness))

            if(forma_selecao == 0):
                pais = EstrategiaSelecao.f_fitness(populacao, self.tamanho_populacao, fitness)
            else:
                pais = EstrategiaSelecao.torneio(populacao, fitness)

            pop_cruzamento = self.cruzamento(pais, pontos)
            populacao = self.mutacao(pop_cruzamento)

            # print("Geração {0} - Melhor fitness: {1}".format(i, min(fitness)))

        return min(fitness)
