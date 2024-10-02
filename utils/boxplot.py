import matplotlib.pyplot as plt

class Boxplot:

    data = []

    def adicionar_dados(self, fitness_iteracao):
        self.data.append(fitness_iteracao)

    def exibir_boxplot(self):
        plt.boxplot(self.data) 
        plt.title('Boxplot de Execuções em Diferentes Cenários', fontsize=14)
        plt.xlabel('Cenários', fontsize=12)
        plt.ylabel('Valores das Execuções', fontsize=12)
        plt.show()
