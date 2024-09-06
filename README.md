# Análise de Dados dos Municípios do Brasil

Este projeto realiza uma análise de dados sobre municípios do Brasil utilizando dados fictícios gerados por inteligência artificial. O objetivo é explorar e visualizar os dados para obter insights sobre a densidade populacional e outras métricas relevantes. Este programa é destinado a fins de estudo e aprendizado.

![Pandas](https://pandas.pydata.org/pandas-docs/stable/_static/pandas.svg)

## Descrição do Projeto

O projeto utiliza um conjunto de dados CSV fictícios contendo informações sobre municípios brasileiros, incluindo as seguintes colunas:
- `Cidade`: Nome da cidade
- `Estado`: Sigla do estado
- `População`: Número de habitantes
- `Área`: Área em metros quadrados

**Nota Importante**: Os dados utilizados neste projeto são fictícios e foram gerados por inteligência artificial para fins de estudo e aprendizado.

## Funcionalidades

1. **Leitura e Pré-processamento dos Dados**:
   - Leitura dos dados a partir de um arquivo CSV.
   - Verificação de valores nulos e substituição de valores zero em área para evitar divisões por zero.
   
2. **Análise Estatística**:
   - Estatísticas descritivas das colunas numéricas.
   - Verificação de valores ausentes.
   
3. **Visualizações**:
   - Gráfico da média da população por estado.
   - Gráfico do desvio padrão da área por estado.
   - Gráfico da soma da população por cidade em São Paulo.
   - Gráfico da área média por cidade em São Paulo.
   - Gráfico de dispersão da relação entre população e área.
   - Gráfico da densidade populacional média por estado.
   - Gráfico da densidade populacional média por cidade em São Paulo.

## Instruções de Uso

1. **Preparação do Ambiente**:
   - Certifique-se de que você tem o Python instalado.
   - Instale as bibliotecas necessárias com o seguinte comando:
     ```bash
     pip install pandas matplotlib
     ```

2. **Execução do Código**:
   - Faça o upload do arquivo CSV com os dados fictícios.
   - Execute o código presente no notebook `codigo_estudos_dados.py` para realizar a análise.

3. **Visualização dos Resultados**:
   - Após executar o código, você visualizará gráficos e estatísticas.
