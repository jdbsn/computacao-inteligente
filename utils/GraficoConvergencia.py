import matplotlib.pyplot as plt

class GraficoConvergencia:

    def __init__(self):
        self.cenarios = []

    def adicionar_dados(self, data, label):
        self.cenarios.append((data, label))

    def exibir_convergencia(self, titulo):
        plt.figure(figsize=(10, 6))

        for data, label in self.cenarios:
            plt.plot(data, label=label)

        plt.title(titulo)
        plt.xlabel('Iterações')
        plt.ylabel('Fitness')
        plt.legend()
        plt.grid(True)
        plt.show()
