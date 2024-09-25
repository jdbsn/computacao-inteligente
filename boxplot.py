import matplotlib.pyplot as plt

class Boxplot:

    data = []

    def adicionar_dados(self, fitness_iteracao):
        self.data.append(fitness_iteracao)

    def exibir_boxplot(self):
        plt.boxplot(self.data) 
        plt.title('Basic Boxplot') 
        plt.show()
