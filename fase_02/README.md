# Estrutura de Diretórios para Projetos de Data Science

## Visão Geral

Este repositório oferece uma estrutura padrão para organização de projetos de Data Science. A estrutura foi desenhada para ser flexível e adequada a diferentes tipos de projetos, garantindo clareza, reprodutibilidade e fácil colaboração. Este README também fornece exemplos de documentos que podem ser armazenados em cada diretório.

## Estrutura de Diretórios

```plaintext
    project-name/
    │
    ├── data/
    │   ├── external/          # Dados de fontes externas, não brutos, mas complementares
    │   ├── interim/           # Dados intermediários durante o processo de ETL
    │   ├── processed/         # Dados processados e prontos para análise
    │   └── raw/               # Dados brutos, não processados
    │
    ├── docs/                  # Documentação do projeto, como especificações, manuais, etc.
    │    ├── data_dictionary.md # Dicionário de dados
    │    └── specifications.md # Especificações do projeto
    │ 
    ├── environment/           # Arquivos relacionados ao ambiente, como conda environment e requirements
    │   ├── environment.yml    # Arquivo de configuração do ambiente conda
    │   ├── requirements.txt   # Lista de pacotes pip (para compatibilidade)
    │   └── setup.py           # Script para configurar o pacote se necessário
    │   
    ├── notebooks/             # Jupyter Notebooks para exploração e análises iniciais
    │   ├── analysis/          # Notebooks para análises exploratórias
    │   ├── exploration/       # Notebooks para exploração de dados
    │   ├── final/             # Notebooks finais, com análises e visualizações principais
    │   └── visualization/     # Notebooks para visualização de dados
    │
    ├── output/                # Resultados das análises, como gráficos, tabelas, relatórios
    │   ├── figures/           # Gráficos gerados durante a análise
    │   ├── reports/           # Relatórios e documentos de análise
    │   └── tables/            # Tabelas geradas durante a análise
    │
    ├── scripts/               # Scripts de Python para manipulação de dados, treinamento de modelos, etc.
    │   ├── data_analysis/     # Scripts para análise de dados
    │   ├── data_processing/   # Scripts para limpeza e transformação de dados
    │   ├── data_visualization/ # Scripts para visualização de dados
    │   └── utils/             # Funções e classes reutilizáveis
    │
    ├── src/                   # Código-fonte do projeto, incluindo módulos reutilizáveis e funções
    │   ├── __init__.py        # Arquivo que torna o diretório um pacote Python
    │   ├── data_loader.py     # Funções para carregar e pré-processar dados
    │   ├── train_model.py     # Código para treinar modelos
    │   └── evaluate_model.py  # Código para avaliar modelos
    │
    ├── tests/                 # Testes unitários e de integração para o código
    │   ├─ integration/        # Testes de integração   
    │   └── unit/              # Testes unitários
    │
    ├── .gitignore             # Arquivo para especificar quais arquivos/pastas não devem ser versionados pelo git
    │
    ├── LICENSE.md             # Licença do projeto
    │
    └── README.md              # Documentação principal do projeto
```
## Descrição das Pastas

- **data/**: Diretório onde todos os dados do projeto são armazenados.
    - **external/**: Dados de fontes externas, como APIs, bancos de dados, e arquivos de terceiros. Exemplo: `external_data.csv`.
    - **interim/**: Dados intermediários gerados durante o processo de ETL (Extract, Transform, Load). Exemplo: `interim_data.csv`.
    - **processed/**: Dados processados e prontos para análise. Exemplo: `processed_data.csv`.
    - **raw/**: Dados brutos, não processados. Exemplo: `raw_data.csv`.
  
- **docs/**: Diretório para armazenar documentos relacionados ao projeto, como especificações, dicionarios de dados, e manuais. 

- **environment/**: Diretório para armazenar arquivos de configuração do ambiente, como `environment.yml` para configuração com conda, e `requirements.txt` para instalação de pacotes com pip.

- **notebooks/**: Diretório para armazenar notebooks Jupyter usados para a exploração de dados, desenvolvimento de modelos, e visualizações preliminares.
    - **analysis/**: Notebooks para análises exploratórias. Exemplo: `exploratory_analysis.ipynb`.
    - **exploration/**: Notebooks para exploração de dados. Exemplo: `data_exploration.ipynb`.
    - **final/**: Notebooks finais, com análises e visualizações principais. Exemplo: `final_analysis.ipynb`.
    - **visualization/**: Notebooks para visualização de dados. Exemplo: `data_visualization.ipynb`. 

- **output/**: Diretório para armazenar os resultados das análises, como gráficos, relatórios, e tabelas geradas. Exemplo: `analysis_plot.png`.
    - **figures/**: Gráficos gerados a partir das análises. Exemplo: `plot.png`.
    - **reports/**: Relatórios gerados a partir das análises. Exemplo: `report.pdf`.
    - **tables/**: Tabelas geradas a partir das análises. Exemplo: `summary_table.csv`.

- **scripts/**: Diretório para scripts Python que executam tarefas específicas como preparação de dados, engenharia de features, e treinamento de modelos.
    - **data_analysis/**: Scripts para análise de dados. Exemplo: `data_analysis.py`.
    - **data_processing/**: Scripts para limpeza e transformação de dados. Exemplo: `data_preprocessing.py`.
    - **data_visualization/**: Scripts para visualização de dados. Exemplo: `data_visualization.py`.
    - **utils/**: Funções e classes reutilizáveis. Exemplo: `utils.py`.

- **src/**: Diretório contendo o código-fonte do projeto. Este código geralmente é modular e pode ser reutilizado. Exemplo: `data_loader.py`.

- **tests/**: Diretório para testes unitários e de integração, assegurando a qualidade do código.
    - **integration/**: Testes de integração. Exemplo: `test_integration.py`.
    - **unit/**: Testes unitários. Exemplo: `test_unit.py`.

- **.gitignore**: Arquivo para listar arquivos e diretórios que não devem ser versionados.
  
- **LICENSE.md**: Arquivo contendo a licença do projeto.
  
- **README.md**: Documentação principal do projeto, contendo uma descrição geral, instruções de uso, e informações de contato.

## Uso dos Arquivos .gitkeep
Os arquivos .gitkeep foram incluídos em todos os diretórios vazios para garantir que esses diretórios sejam rastreados pelo Git. O Git não versiona automaticamente diretórios vazios, portanto, o .gitkeep serve como um placeholder para assegurar que a estrutura do projeto seja mantida quando o repositório é clonado. Quando você adicionar arquivos reais nesses diretórios, você pode remover o .gitkeep ou deixá-lo no diretório, conforme sua preferência.
  
## Como Usar

Para utilizar essa estrutura em seus projetos:

### 1. Clone o repositório para sua máquina local:
   ```bash
      git clone https://github.com/seu-usuario/estrutura-data-science.git
   ```
### 2. Renomeie o diretório clonado para o nome do seu projeto:
   ```bash
   mv estrutura-data-science/ nome-do-seu-projeto/
   ```
### 3. Personalize o README e a estrutura de diretórios conforme necessário.

Exemplo de README.md:

```markdown
    # Projeto de Análise de Dados

    Este projeto tem como objetivo analisar dados de vendas de uma empresa e prever as vendas futuras.

    ## Estrutura de Diretórios

    - **data/**: Dados brutos, processados e intermediários.
    - **notebooks/**: Notebooks Jupyter para exploração de dados.
    - **scripts/**: Scripts Python para preparação de dados e treinamento de modelos.
    - **src/**: Código-fonte do projeto.
    - **tests/**: Testes unitários e de integração.
    - **results/**: Resultados das análises.
    - **environment/**: Configuração do ambiente.

    ## Configuração

    1. Instale os pacotes necessários:
    ```bash
    conda env create -f environment/environment.yml
    ```
    2. Ative o ambiente conda:
    ```bash
        conda activate nome-do-ambiente
        ```
    3. Execute os scripts e notebooks conforme necessário.

    ## Contribuições

    Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request com sugestões ou melhorias.

    ## Licença

    Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

    ## Contato

    - **Nome:** SeuNome
    - **Email:** EndereçoDeEmail@exemplo.com
    - **LinkedIn:** [linkedin.com/in/nome](https://www.linkedin.com/in/nome)
```
   
### 4. Comece a adicionar seus dados, notebooks, scripts e código-fonte ao projeto.

## Contribuições

Contribuições são bem-vindas! Por favor, abra uma issue ou envie um pull request com sugestões ou melhorias.

### Agradecimentos

Este projeto contou com a contribuição de:

- [Janaína Cazuza](https://github.com/janainacazuza/janainacazuza)

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Contato
https://www.linkedin.com/in/janainacazuza/
janainamartinscazuza@gmail.com




