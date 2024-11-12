Projeto Integrado II - Ciência de Dados
Bem-vindo ao repositório do Projeto Integrado II para o curso de Ciência de Dados. Este projeto visa aplicar as habilidades adquiridas ao longo do curso em um estudo de caso prático, com foco na análise de dados e visualização de informações para tomada de decisões.

Objetivo do Projeto
O objetivo deste projeto é analisar e visualizar dados relacionados a um supermercado, com ênfase nas operações de vendas e custos. A análise busca gerar insights sobre a performance dos produtos, as margens de lucro e a eficiência logística.

Tecnologias Utilizadas
Este projeto foi desenvolvido utilizando as seguintes tecnologias:

Python: Linguagem de programação utilizada para análise de dados.
Pandas: Biblioteca para manipulação de dados.
Matplotlib e Seaborn: Bibliotecas para visualização de dados.
Streamlit: Framework para criar aplicações interativas com Python.
openpyxl: Para leitura de arquivos Excel (.xlsx).
Estrutura do Projeto
A estrutura do projeto é a seguinte:

bash
Copiar código
/ProjetoIntegradoII
    /venv                  # Ambiente virtual
    /tem.py                # Script principal do projeto
    /tem.xlsx              # Arquivo de dados do supermercado
    /requirements.txt      # Dependências do projeto
    /README.md             # Este arquivo
tem.py
O script principal onde a análise de dados é realizada. Ele importa os dados de um arquivo Excel (tem.xlsx), limpa e organiza os dados, e gera insights sobre vendas, margens de lucro, custos de frete e outros.

tem.xlsx
Arquivo Excel contendo os dados de vendas, produtos, custos e outras métricas utilizadas na análise.

requirements.txt
Arquivo com as dependências necessárias para rodar o projeto. Para instalar todas as dependências, basta rodar:

Copiar código
pip install -r requirements.txt
Como Executar o Projeto
Clone o repositório:

bash
Copiar código
git clone https://github.com/joaop92/ProjetoIntegradoII.git
cd ProjetoIntegradoII
Crie e ative um ambiente virtual (opcional, mas recomendado):

Para Windows:

bash
Copiar código
python -m venv venv
.\venv\Scripts\activate
Para macOS/Linux:

bash
Copiar código
python3 -m venv venv
source venv/bin/activate
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Execute o projeto:

Execute o script com o Streamlit para iniciar a aplicação interativa:

bash
Copiar código
streamlit run tem.py
O Streamlit abrirá uma interface no seu navegador para visualização e interação com os dados.

Funcionalidades
Análise de Preços de Venda: Visualize a distribuição dos preços de venda dos produtos.
Margem de Lucro: Análise detalhada da margem de lucro de cada produto.
Produtos Mais Vendidos: Descubra quais produtos tiveram o maior volume de vendas.
Receita Bruta e Líquida: Comparação das receitas de vendas de cada produto.
Custo de Frete: Identifique os custos de frete médios por produto.

