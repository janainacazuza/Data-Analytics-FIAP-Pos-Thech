# Data Analytics - Pós-Tech FIAP

## Visão Geral

Bem-vindo ao repositório do meu projeto desenvolvido durante a Fase 01 da pós-graduação em Data Analytics na FIAP. Nesta fase, o foco é a Análise e Exploração de Dados, onde aplico técnicas avançadas para adquirir, limpar e visualizar conjuntos de dados reais. Este projeto documenta minha evolução no entendimento e aplicação de processos de ETL (Extract, Transform, Load), manipulação de dados, e criação de visualizações que suportam a tomada de decisões baseada em dados.

## Fase 1 - Data Analysis and Exploration

### Aula 1 - Aquisição, Limpeza e Tratamento de Dados Reais

Nesta primeira etapa, fui introduzido aos conceitos fundamentais de aquisição e preparação de dados. Trabalhei com um conjunto de dados obtido do [DATASUS](https://datasus.saude.gov.br/acesso-a-informacao/producao-hospitalar-sih-sus/), focado nos valores iniciais liberados para internações hospitalares no Brasil. Abaixo estão os principais tópicos abordados:

#### 1. Ferramentas Utilizadas

- **Pandas**: Para manipulação e análise de dados.
- **Numpy**: Para operações matemáticas e manipulação de arrays.
- **Matplotlib**: Para a visualização de dados.

#### 2. Aquisição e Preparação dos Dados

Os dados brutos foram extraídos e transformados para se adequar ao padrão brasileiro, utilizando vírgula como separador decimal e ponto como separador de milhar. Este ajuste foi essencial para garantir a legibilidade e precisão nas análises subsequentes.

#### 3. Verificação dos Dados

Antes de realizar qualquer análise, assegurei a integridade dos dados através de:
- **Exploração Inicial**: Entendimento da estrutura dos dados e identificação das variáveis.
- **Validação de Consistência**: Verificação de valores ausentes, duplicações e anomalias.
- **Sumarização Estatística**: Geração de estatísticas descritivas das variáveis para identificar padrões e outliers.

#### 4. **Tratamento dos Dados - ETL (Extract, Transform, Load)**

Uma parte crucial do meu aprendizado foi o processo de **ETL** aplicado aos dados para garantir que a análise seja baseada em dados de qualidade. As principais etapas incluíram:

##### 4.1 Criação de Cópia do DataFrame Original

- **Objetivo**: Preservar o dataset original e garantir que todas as transformações fossem rastreáveis e reversíveis. Esta etapa corresponde à fase de *Extract* e *Load* no processo de ETL, onde os dados são extraídos da fonte original e carregados para um ambiente seguro de manipulação.

##### 4.2 Tratamento dos Dados Categóricos

- **Manutenção da Coluna Categórica**: A coluna "Unidade da Federação" foi mantida como string, já que é uma variável categórica.
- **Limpeza dos Valores Categóricos**: Remoção de números e espaços desnecessários para garantir que apenas o nome do estado permanecesse na coluna. Essa etapa faz parte da fase de *Transform* no processo de ETL.

##### 4.3 Tratamento dos Dados Quantitativos

- **Correção de Valores Ausentes**: Identifiquei e preenchi valores faltantes na coluna `2009/Set` utilizando a média dos valores adjacentes.
- **Conversão de Tipos**: Assegurei que todos os valores na coluna `2009/Set` fossem convertidos para tipos numéricos adequados. Ambas as etapas são fundamentais na fase de *Transform* do processo de ETL.

##### 4.4 Criação de Cópia do DataFrame Após Tratamento

- **Objetivo**: Garantir que o DataFrame tratado fosse usado para todas as análises subsequentes, preservando a integridade das transformações realizadas. Esta cópia final é uma representação do conjunto de dados pronto para análise, finalizando o processo de *ETL*.

### Aula 2 - Primeiras Visualizações de Dados

A segunda aula introduziu-me à visualização de dados, uma habilidade essencial para comunicar insights de forma clara e impactante.

#### 2.1 Visualização Inicial de Gráficos

- **Plotagem de Dados**: Criei gráficos de barras para visualizar os valores por Unidade da Federação, começando com os dados de `2008/Ago`.

#### 2.2 Desafios

- **Desafio 01**: Plotar gráficos para o mês mais recente, aplicando os conceitos aprendidos.
- **Desafio 02**: Ajustar as legendas dos estados no eixo x para melhor legibilidade, rotacionando-as em 45º.

## Habilidades Desenvolvidas

- **Manipulação e Análise de Dados:** Proficiência no uso de Python e Pandas para manipulação e análise de dados.

- **Processo de ETL:** Experiência prática em extração, transformação e carregamento de dados, garantindo a qualidade dos dados para análise.

- **Visualização de Dados:** Habilidade em criar visualizações claras e informativas utilizando Matplotlib.

## Ferramentas Utilizadas

- **Python 3.12.3**
- **Jupyter Notebook**
- **Pandas**
- **Matplotlib**
- **Ambiente `conda`**: Configurado para gerenciar as dependências e garantir a reprodutibilidade do ambiente de desenvolvimento.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias ou sugestões.

## Licença
Este projeto é distribuído sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.



## Contato

- **Nome:** Janaína Cazuza
- **Email:** janainamartinscazuza@gmail.com
- **LinkedIn:** [linkedin.com/in/janainacazuza](https://www.linkedin.com/in/janainacazuza/)

