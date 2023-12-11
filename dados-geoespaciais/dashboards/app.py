import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Configurando a largura total da página
    st.set_page_config(layout="wide")

    # Centralizando o título
    st.markdown("<h3 style='text-align: center; color: black;'>Furtos Contra o Patrimônio no Distrito Federal</h3>", unsafe_allow_html=True)

    # Carregando os dados do arquivo CSV
    path = "gdf_furtos_gsp.csv"
    df = carregar_dados(path)

    # Gráfico de População por Cidade
    st.markdown("<h5 style='text-align: center; color: black;'>População do Distrito Federal</h5>", unsafe_allow_html=True)

    exibir_grafico_populacao(df)

    # Mapa 1 e Mapa 2 (Mapa de Calor)
    st.markdown("<h5 style='text-align: center; color: black;'>Mapas</h5>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Mapa 1
    with col1:
        exibir_mapa_html("http://127.0.0.1:5501/dados-geoespaciais/qtd_furtos_DF.html")

    # Mapa 2 (Mapa de Calor)
    with col2:
        exibir_mapa_html("http://127.0.0.1:5501/dados-geoespaciais/heatmap_furtos_contra_patrimonio.html")

    # Tabela de Ocorrências por Cidade
    st.markdown("<h5 style='text-align: center; color: black;'>Informações sobre as Cidades</h5>", unsafe_allow_html=True)

    st.dataframe(df)

    # Gráfico de Média Geral
    st.markdown("<h5 style='text-align: center; color: black;'>Média de Furtos por Cidade</h5>", unsafe_allow_html=True)
    # Menu drop-down acima do gráfico
    cidade_selecionada_geral = st.selectbox("Selecione a Cidade desejada:", df['CID_MUN'].unique())
    exibir_grafico_media_geral(df, cidade_selecionada_geral)

    # Gráficos das 5 maiores e 5 menores médias
    st.markdown("<h5 style='text-align: center; color: black;'>Maiores e Menores médias</h5>", unsafe_allow_html=True)
    exibir_graficos_maior_menor_media(df)

def carregar_dados(path):
    # Carregando os dados do arquivo CSV
    df = pd.read_csv(path)
    return df

def exibir_grafico_populacao(df):
    # Criando o gráfico com tamanho de figura igual ao de Média de Furtos por Cidade
    fig, ax = plt.subplots(figsize=(22, 9))  # Ajuste aqui
    
    # Adicionando os valores nas barras com vírgula substituída por ponto
    sns.barplot(x='CID_MUN', y='População', data=df, ax=ax, color='gray')  # Todas as barras em cinza
    
    # Adicionando os valores acima das barras
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}'.replace(',', '.'), (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 16), textcoords='offset points')

    # Ajustando layout
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.tight_layout()

    # Adicionando interatividade com o drop-down
    selected_city = st.selectbox("Selecione uma cidade:", df['CID_MUN'])
    
    # Adicionando cor destacada para a cidade selecionada
    x_ticks = ax.get_xticks()
    selected_index = int(np.where(x_ticks == df[df['CID_MUN'] == selected_city].index[0])[0])
    for i, bar in enumerate(ax.patches):
        if bar.get_height() > 0 and i == selected_index:
            bar.set_color('red')

    # Exibindo o gráfico
    st.pyplot(fig)

def exibir_mapa_html(link_mapa):
    st.markdown(f'<iframe src="{link_mapa}" width="100%" height="300"></iframe>', unsafe_allow_html=True)

def exibir_grafico_media_geral(df, cidade_selecionada):
    # Lógica para mudar a cor da cidade selecionada
    cores = ['blue' if cidade == cidade_selecionada else 'gray' for cidade in df['CID_MUN']]

    # Criando o gráfico
    fig, ax = plt.subplots(figsize=(18, 6))
    bars = ax.bar(df['CID_MUN'], df['Média'], color=cores)
    ax.set_xlabel('Cidades')
    ax.set_ylabel('Médias')
    #ax.set_title('Média de Furtos por Cidade')

    # Adicionando os valores acima das barras
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.2f}', ha='center', va='bottom', fontsize=8, color='black')

    # Ajustando layout para incluir a inclinação dos nomes das cidades
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.tight_layout()

    # Exibindo o gráfico
    st.pyplot(fig)

def exibir_graficos_maior_menor_media(df):
    # Ordenando o DataFrame por média
    df_ordenado = df.sort_values(by='Média')

    # 5 Maiores Médias
    fig, ax = plt.subplots(1, 2, figsize=(12, 2))  # Alteração aqui
    ax[0].barh(df_ordenado.tail()['CID_MUN'], df_ordenado.tail()['Média'], color='red')  # Alteração para barras horizontais
    ax[0].set_xlabel('Médias')
    ax[0].set_ylabel('Cidades')
    ax[0].set_title('5 Maiores Médias de Furtos por Cidade')

    # 5 Menores Médias
    ax[1].barh(df_ordenado.head()['CID_MUN'], df_ordenado.head()['Média'], color='green')  # Alteração para barras horizontais
    ax[1].set_xlabel('Médias')
    ax[1].set_ylabel('Cidades')
    ax[1].set_title('5 Menores Médias de Furtos por Cidade')

    # Ajustando layout para incluir a inclinação dos nomes das cidades
    plt.tight_layout()
    plt.subplots_adjust(wspace=0.7)  # Ajuste do espaço entre os gráficos

    # Exibindo os gráficos
    st.pyplot(fig)

if __name__ == "__main__":
    main()


