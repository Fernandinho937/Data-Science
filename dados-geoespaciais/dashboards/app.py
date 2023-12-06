import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Dashboard de Furtos Contra o Patrimônio')

    # Carregando os dados do arquivo CSV
    path = "gdf_furtos_gsp.csv"
    df = pd.read_csv(path)

    # Variáveis de sessão para rastrear o estado dos elementos
    mostrar_tabela = st.session_state.get("mostrar_tabela", False)
    mostrar_grafico = st.session_state.get("mostrar_grafico", False)
    mostrar_mapa = st.session_state.get("mostrar_mapa", False)

    # Botões no sidebar para Exibir/Ocultar Tabela,
    # Exibir/Ocultar Gráfico População por Cidade e
    # Exibir/Ocultar Mapa HTML
    if st.sidebar.button("Tabela"):
        mostrar_tabela = not mostrar_tabela
        st.session_state.mostrar_tabela = mostrar_tabela
        st.session_state.mostrar_grafico = False
        st.session_state.mostrar_mapa = False

    if st.sidebar.button("Gráfico"):
        mostrar_grafico = not mostrar_grafico
        st.session_state.mostrar_grafico = mostrar_grafico
        st.session_state.mostrar_tabela = False
        st.session_state.mostrar_mapa = False

    if st.sidebar.button("Mapa"):
        mostrar_mapa = not mostrar_mapa
        st.session_state.mostrar_mapa = mostrar_mapa
        st.session_state.mostrar_tabela = False
        st.session_state.mostrar_grafico = False

    # Exibir ou ocultar tabela com base no estado
    if mostrar_tabela:
        exibir_tabela(df)

    # Exibir ou ocultar gráfico com base no estado
    if mostrar_grafico:
        exibir_grafico_populacao(df)

    # Adicionar o mapa HTML usando uma tag iframe
    if mostrar_mapa:
        exibir_mapa_html()

def exibir_tabela(df):
    st.header('Tabela de Ocorrências por Cidade')
    st.dataframe(df)

def exibir_grafico_populacao(df):
    st.header('Gráfico de População por Cidade')

    # Criando o gráfico com tamanho de figura maior
    fig, ax = plt.subplots(figsize=(18, 12))
    sns.barplot(x='CID_MUN', y='População', data=df, ax=ax)

    # Adicionando os valores nas barras
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 16), textcoords='offset points')

    # Ajustando layout
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.tight_layout()

    # Exibindo o gráfico
    st.pyplot(fig)

def exibir_mapa_html():
    # Substitua 'caminho/para/seu/mapa.html' pelo caminho real do seu mapa HTML
    st.markdown('<iframe src="http://127.0.0.1:5501/dados-geoespaciais/qtd_furtos_DF.html" width="100%" height="300"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()







'''
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    st.title('Dashboard de Furtos Contra o Patrimônio')

    # Carregando os dados do arquivo CSV
    path = "gdf_furtos_gsp.csv"
    df = pd.read_csv(path)

    # Variáveis de sessão para rastrear o estado dos elementos
    mostrar_tabela = st.session_state.get("mostrar_tabela", False)
    mostrar_grafico = st.session_state.get("mostrar_grafico", False)

    # Botões no sidebar para Exibir/Ocultar Tabela,
    # Exibir/Ocultar Gráfico População por Cidade e
    # Exibir Mapa HTML
    if st.sidebar.button("Exibir/Ocultar Tabela"):
        mostrar_tabela = not mostrar_tabela
        mostrar_grafico = False
        st.session_state.mostrar_tabela = mostrar_tabela
        st.session_state.mostrar_grafico = mostrar_grafico

    if st.sidebar.button("Exibir/Ocultar Gráfico População por Cidade"):
        mostrar_grafico = not mostrar_grafico
        mostrar_tabela = False
        st.session_state.mostrar_tabela = mostrar_tabela
        st.session_state.mostrar_grafico = mostrar_grafico

    # Exibir ou ocultar tabela com base no estado
    if mostrar_tabela:
        exibir_tabela(df)

    # Exibir ou ocultar gráfico com base no estado
    if mostrar_grafico:
        exibir_grafico_populacao(df)

    # Adicionar o mapa HTML usando uma tag iframe
    exibir_mapa_html()

def exibir_tabela(df):
    st.header('Tabela de Ocorrências por Cidade')
    st.dataframe(df)

def exibir_grafico_populacao(df):
    st.header('Gráfico de População por Cidade')

    # Criando o gráfico com tamanho de figura maior
    fig, ax = plt.subplots(figsize=(18, 12))
    sns.barplot(x='CID_MUN', y='População', data=df, ax=ax)

    # Adicionando os valores nas barras
    for p in ax.patches:
        ax.annotate(f'{int(p.get_height()):,}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 16), textcoords='offset points')

    # Ajustando layout
    plt.xticks(rotation=45, ha='right', rotation_mode='anchor')
    plt.tight_layout()

    # Exibindo o gráfico
    st.pyplot(fig)

def exibir_mapa_html():
    # Substitua 'caminho/para/seu/mapa.html' pelo caminho real do seu mapa HTML
    st.markdown('<iframe src="http://127.0.0.1:5501/dados-geoespaciais/qtd_furtos_DF.html" width="100%" height="600"></iframe>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()




'''
