import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st


# Carregar o arquivo Excel
df = pd.read_excel('tem.xlsx')

# Filtro interativo para selecionar o produto
produto_selecionado = st.selectbox('Escolha um Produto', df['Produto'].unique())

# Exibir dados filtrados
produto_filtrado = df[df['Produto'] == produto_selecionado]
st.write(produto_filtrado)



# Exibir as primeiras linhas e os nomes das colunas do DataFrame
st.write(df.head())
st.write("Nomes das colunas:", df.columns)

# Limpeza dos dados
df.fillna(0, inplace=True)
df.drop_duplicates(inplace=True)

# Ajuste para conversão de colunas financeiras, caso estejam como string com "R$"
for coluna in ['Preço Produto (R$)', 'Preço Venda (R$)', 'Custo Frete (R$)', 'Salário Funcionário (R$)', 
               'Receita Bruta (R$)', 'Receita Líquida (R$)', 'Margem de Lucro (R$)']:
    df[coluna] = pd.to_numeric(df[coluna], errors='coerce')

# 1. Distribuição dos preços de venda
fig1, ax1 = plt.subplots(figsize=(10, 6))
sns.histplot(df['Preço Venda (R$)'], bins=30, kde=True, ax=ax1)
ax1.set_title('Distribuição dos Preços de Venda')
ax1.set_xlabel('Preço Venda (R$)')
st.pyplot(fig1)

# 2. Distribuição da Margem de Lucro
fig2, ax2 = plt.subplots(figsize=(10, 6))
sns.histplot(df['Margem de Lucro (R$)'], bins=30, kde=True, ax=ax2)
ax2.set_title('Distribuição da Margem de Lucro')
ax2.set_xlabel('Margem de Lucro (R$)')
st.pyplot(fig2)

# 3. Produto com maior quantidade de vendas
produto_mais_vendido = df.groupby('Produto')['Quantidade Vendida'].sum().idxmax()
quantidade_vendida = df.groupby('Produto')['Quantidade Vendida'].sum().max()
st.write(f"Produto mais vendido: {produto_mais_vendido} com {quantidade_vendida} unidades vendidas.")

# 4. Produto com maior receita bruta
produto_maior_receita = df.groupby('Produto')['Receita Bruta (R$)'].sum().idxmax()
receita_maxima = df.groupby('Produto')['Receita Bruta (R$)'].sum().max()
st.write(f"Produto com maior receita bruta: {produto_maior_receita} com receita de R${receita_maxima:.2f}")

# 5. Produtos mais lucrativos (top 5)
produtos_lucrativos = df.groupby('Produto')['Margem de Lucro (R$)'].sum().sort_values(ascending=False).head(5)
st.write("\nTop 5 produtos mais lucrativos:")
st.write(produtos_lucrativos)

# 6. Frete médio por produto
frete_medio = df.groupby('Produto')['Custo Frete (R$)'].mean()
st.write("\nFrete médio por produto:")
st.write(frete_medio)

# Visualização dos 5 produtos mais lucrativos
fig3, ax3 = plt.subplots(figsize=(10, 6))
produtos_lucrativos.plot(kind='bar', color='skyblue', ax=ax3)
ax3.set_title('Top 5 Produtos Mais Lucrativos')
ax3.set_xlabel('Produto')
ax3.set_ylabel('Margem de Lucro Total (R$)')
ax3.set_xticklabels(produtos_lucrativos.index, rotation=45)
st.pyplot(fig3)

# Visualização do frete médio por produto (Top 5)
fig4, ax4 = plt.subplots(figsize=(10, 6))
frete_medio.sort_values(ascending=False).head(5).plot(kind='bar', color='lightgreen', ax=ax4)
ax4.set_title('Top 5 Produtos com Maior Custo Médio de Frete')
ax4.set_xlabel('Produto')
ax4.set_ylabel('Custo Médio de Frete (R$)')
ax4.set_xticklabels(frete_medio.sort_values(ascending=False).head(5).index, rotation=45)
st.pyplot(fig4)


# Exibir gráfico com o filtro
plt.figure(figsize=(10, 6))
sns.histplot(produto_filtrado['Preço Venda (R$)'], bins=30, kde=True)
plt.title(f'Distribuição de Preço - {produto_selecionado}')
st.pyplot(plt)