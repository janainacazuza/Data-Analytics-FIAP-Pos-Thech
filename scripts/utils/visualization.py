#importando as bibliotecas
import os
import sys 
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import numpy as np

# Função para plotar gráfico de gastos por estado
def plot_state_spending(data):

    # Criando o gráfico
    axis = data.T.plot(figsize=(12,6))

    # Definindo uma paleta de cores personalizada
    colorsofme = ['#F90333', '#50AAA6', '#1155EA', '#EA800A', '#83F921', '#8D9687', '#5E0375']

    # Definindo as cores das linhas    
    for i, line in enumerate(axis.get_lines()):
        line.set_color(colorsofme[i])

    #Colocando grid no gráfico e cofigurando o grid
    plt.grid(True, which='major', linestyle='dotted', linewidth='0.5', color='gray')
    
    # Estabelecendo os limites do eixo Y
    plt.ylim(0, max(data.max()) * 1.1)

    # Estabelecendo o eixo x para ticks de 12 meses
    plt.xticks(np.arange(0, len(data.columns), 12), data.columns[::12], rotation=45)

    # Configurando o gráfico
    plt.title('Atendimentos no SUS por Ano/Mês Processamento')
    plt.xlabel('Ano/Mês Processamento')
    plt.ylabel('Total Gasto')
    plt.gca().xaxis.set_tick_params(labelsize=10)
    plt.gca().yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.2f}'))
    plt.legend(title='Estados', title_fontsize='x-large', fontsize='x-large')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    plt.show()

    
    