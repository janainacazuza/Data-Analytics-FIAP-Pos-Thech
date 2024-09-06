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

    # Estabelecendo os limites do eixo Y
    plt.ylim(0, max(data.max()) + 1.1 * max(data.max()))

    # Estabelecendo o eixp x para ticks de 12 meses
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

    
    