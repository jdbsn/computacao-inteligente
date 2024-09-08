import random

from funcoes import *

def gerar_populacao(tamanho_populacao, dimensoes, min_gene, max_gene):
    populacao = []

    for _ in range(tamanho_populacao):
        cromossomo = []
        for _ in range(dimensoes):    
            cromossomo.append(random.randint(min_gene, max_gene))
        populacao.append(cromossomo)

    return populacao

def f_fitness(populacao, tamanho_populacao, fitness):
    total_fitness = sum(fitness)
    probabilidades = []

    for valor in fitness:
        probabilidades.append(valor/total_fitness)

    selecionados = []
    for _ in range(tamanho_populacao):
        cromossomo_selecionado = roleta(populacao, probabilidades)
        
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
        if sorteio <= limite:
            return cromossomo[i]
        
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

def cruzamento(pais, taxa_cruzamento, dimensoes, pontos = 1):
    resultado = []

    for i in range(0, len(pais), 2):
        valor = random.uniform(0, 1)
        
        if(valor > taxa_cruzamento):
            resultado += pais[i:i+2]  
        else:
            if pontos > dimensoes - 1:
                pontos = dimensoes - 1
            
            pontos_corte = sorted(random.sample(range(1, dimensoes-1), pontos))

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

def mutacao(populacao, taxa_mutacao, min_gene, max_gene):
    for cromossomo in populacao:
       for i in range(len(cromossomo)):
            valor = random.uniform(0, 1)
            if valor <= taxa_mutacao:
                cromossomo[i] = random.randint(min_gene, max_gene)

    return populacao


def alg_genetico(tamanho_populacao, geracoes, dimensoes, taxa_cruzamento, taxa_mutacao, min_gene, max_gene, forma_selecao, pontos):
    
    populacao = gerar_populacao(tamanho_populacao, dimensoes, min_gene, max_gene)

    print("----- População -----")
    print(populacao)

    for i in range(geracoes):
        fitness = [sphere(cromossomo) for cromossomo in populacao]

        if(forma_selecao == 0):
            pais = f_fitness(populacao, tamanho_populacao, fitness)
        else:
            pais = torneio(populacao, fitness)

        pop_cruzamento = cruzamento(pais, taxa_cruzamento, dimensoes, pontos)
        populacao = mutacao(pop_cruzamento, taxa_mutacao, min_gene, max_gene)

        print("Geração {0} - Melhor fitness: {1}".format(i, min(fitness)))

    return min(populacao, key=sphere)

print("Selecione forma de seleção: \n1 - Roleta | 2 - Torneio (padrão)")
input_selecao = int(input())
print("Informe quantos pontos de corte serão realizados: ")
input_pontos = int(input())

resultado = alg_genetico(30, 10000, 30, 0.9, 0.01, -100, 100, input_selecao, input_pontos)

print("----- Melhor resultado -----")
print(resultado)
# consertar quando tamanho da população for impar
