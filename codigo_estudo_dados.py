import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn-v0_8-dark")

from google.colab import files
arq = files.upload()

# Criando o DataFrame
df = pd.read_csv("municipios_brasil.csv")

# Adicionando uma nova coluna para a densidade populacional por metro quadrado
# Evita divisão por zero substituindo valores zero em 'Área' por NaN e, depois, preenchendo com a média
df['Área'].replace(0, pd.NA, inplace=True)
df['Densidade'] = df['População'] / df['Área']

# Preenchendo possíveis valores NaN em 'Área' (caso haja) com a média da área (opcional)
df['Área'].fillna(df['Área'].mean(), inplace=True)

# Exibindo estatísticas descritivas atualizadas, incluindo a nova coluna
print("Estatísticas descritivas (incluindo densidade):")
print(df.describe())

# Visualizando os 5 primeiros elementos do DataFrame atualizado
print("\nPrimeiros 5 registros (incluindo densidade):")
print(df.head())

# Visualizando a densidade populacional média por estado
estado_densidade_mean = df.groupby('Estado')['Densidade'].mean()
print("\nDensidade populacional média por estado:")
print(estado_densidade_mean)
estado_densidade_mean.plot.bar(title='Densidade Populacional Média por Estado (pessoas por m²)')
plt.xlabel('Estado')
plt.ylabel('Densidade Populacional Média (pessoas por m²)')
plt.show()

# Visualizando a densidade populacional média por cidade em São Paulo
cidade_densidade_mean = df[df['Estado'] == 'São Paulo'].groupby('Cidade')['Densidade'].mean().sort_values()
print("\nDensidade populacional média por cidade em São Paulo:")
print(cidade_densidade_mean)
cidade_densidade_mean.plot.barh(title='Densidade Populacional Média por Cidade em São Paulo (pessoas por m²)')
plt.xlabel('Densidade Populacional Média (pessoas por m²)')
plt.ylabel('Cidade')
plt.show()
