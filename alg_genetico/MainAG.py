import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from alg_genetico.AlgoritmoGenetico import AlgoritmoGenetico


print("Selecione forma de seleção: \n1 - Roleta | 2 - Torneio (padrão)")
input_selecao = int(input())
print("Informe quantos pontos de corte serão realizados: ")
input_pontos = int(input())

algoritmo = AlgoritmoGenetico(30, 20, 30, 0.9, 0.01, -100, 100)

resultado = algoritmo.alg_genetico(input_selecao, input_pontos)

print("----- Melhor resultado -----")
print(resultado)