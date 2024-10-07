import pandas as pd

data = {
    'nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)
print(df)

nomes = df['nome']
print(nomes)

primeira_linha = df.iloc[0]
print(primeira_linha)

subset = df.loc[:1, ['nome', 'Idade']]
print(subset)

filtro = df[df['Idade'] > 23]
print(filtro)

df['Idade em 5 anos'] = df['Idade'] + 5
print(df)

df = df.drop(columns=['Cidade'])
print(df)

df_ordenado = df.sort_values(by='Idade', ascending=False)
print(df_ordenado)

data = {
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Alagoas', 'Sergipe'],
    'Vendas': [200, 150, 300, 400]
}

df_vendas = pd.DataFrame(data)

agrupado = df_vendas.groupby('Cidade').sum()
print(agrupado)

df1 = pd.DataFrame({'Id': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Carlos']})
df2 = pd.DataFrame({'Id': [1, 2, 4], 'Salario': [5000, 6000, 7000]})

df_combined = pd.merge(df1, df2, on='Id', how='inner')
print(df_combined)

import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Carlos'],
    'Idade': [25, 30, 22],
    'Cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

df = pd.DataFrame(data)

nomes = df['Nome']
print(nomes)

##

subset = df[['Nome', 'Cidade']]
print(subset)

primeira_linha = df.iloc[0]
print(primeira_linha)

primeira_duas_linhas = df.iloc[:2]
print(primeira_duas_linhas)

df.at[0, 'Nome'] = 'Ana'
print(df)

df['País'] = 'Brasil'
print(df)

df = df.drop(columns=['Cidade'])
print(df)

df['Idade'] = df['Idade'].apply(lambda x: x + 5)
print(df)

df.loc[1, 'País'] = None

df_limpo = df.dropna()
print(df_limpo)

df_preenchido = df.fillna('Desconhecido')
print(df_preenchido)

df_dup = pd.DataFrame({
    'Nome': ['Ana', 'Ana', 'Carlos'],
    'Idade': [25, 25, 22],
    'País': ['Brasil', 'Brasil', 'Brasil']
})

import pandas as pd 

data = {'Idade':[23, 29, 34, 22, 55]}
df = pd.DataFrame(data) 

media_idade = df['Idade'].mean() 
print(media_idade) 

mediana_idade = df['Idade'].median()
print(mediana_idade)

data = {'Idade':[23, 29, 34, 22, 25, 29]} 
df = pd.DataFrame(data) 

moda_idade = df['Idade'].mode()
print(moda_idade) 

soma_idade = df['Idade'].sum()
print(soma_idade) 

contagem_idade = df['Idade'].count()
print(contagem_idade) 

desvio_padrao_idade = df['Idade'].std()
print(desvio_padrao_idade) 

min_idade = df['Idade'].min()
max_idade = df['Idade'].max()
print(f'Idade minima: {min_idade}, Idade maxima: {max_idade}')

variancia_idade = df['Idade'].var()
print(variancia_idade)
df_sem_duplicatas = df_dup.drop_duplicates()
print(df_sem_duplicatas) 

resumo_estatistico = df_vendas.describe()
print(resumo_estatistico) 

df_vendas['Lucro'] = df_vendas['Vendas'] 

correlacao = df_vendas[['Vendas', 'Lucro']].corr()
print(correlacao) 

covariancia = df_vendas[['Vendas', 'Lucro']].cov() 
print(covariancia) 

df_vendas['Rank'] = df_vendas['Vendas'].rank()
print(df_vendas) 

import pandas as pd 

data = {'Nome' : ['Ana', 'Bruno', None, 'Carlos'],
       'Idade':[23, None, 35,29],
       'Cidade':['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', None]} 

df = pd.DataFrame(data) 
print(df.isnull()) 
print(df.isnull().sum()) 

df_sem_na = df.dropna() 
print(df_sem_na) 

df_sem_na_col = df.dropna(axis=1)
print(df_sem_na_col) 

df['Idade'] = df['Idade'].fillna(df['Idade'].mean()) 
print(df)

df_sem_dup = df_dup.drop_duplicates() 
print(df_sem_dup) 

df_sem_dup_nome = df_dup.drop_duplicates(subset=['Nome'])
print(df_sem_dup_nome) 

data_tipos = {'Produto' : ['A', 'B', 'C'],
              'Preco' : ['10.5', '20.3', '30.2'],
             'Quantidade' : ['1', '2', '3']} 

df_tipos = pd.DataFrame(data_tipos) 

df_tipos['Preco'] = df_tipos['Preco'].astype(float) 
df_tipos['Quantidade'] = df_tipos['Quantidade'].astype(int)
print(df_tipos.dtypes) 

data_espacos = {'Nome' : ['Ana', 'Bruno', 'Carlos'],
               'Cidade' : ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte']}  

df_espacos = pd.DataFrame(data_espacos) 

df_espacos['Nome'] = df_espacos['Nome'].str.strip()
df_espacos['Cidade'] = df_espacos['Cidade'].str.strip()
print(df_espacos) 

data_outliers = {'Idade' : [23, 29, 35, 120, 28, 22, 25]} 

df_outliers = pd.DataFrame(data_outliers) 

media = df_outliers['Idade'].mean() 
desvio_padrao = df_outliers['Idade'].std() 

outliers = df_outliers[(df_outliers['Idade'] > media + 3*desvio_padrao)] 
(df_outliers['Idade'] < media - 3*desvio_padrao) 

df_sem_outliers = df_outliers[(df_outliers['Idade'] <= media + 2*desvio_padrao)
(df_outliers['Idade'] >= media - 2*desvio_padrao)] 
print(df_sem_outliers) 
