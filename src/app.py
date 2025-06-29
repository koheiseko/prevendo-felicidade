import streamlit as st
import pandas as pd

model = pd.read_pickle('models/model_feliz.pkl')

st.markdown('# Descubra a felicidade')

col1, col2, col3 = st.columns(3)

with col1:
    video_game  = st.radio('Curte Video Games?', ['Sim', 'Não'])
    futebol  = st.radio('Curte Futebol?', ['Sim', 'Não'])
   
    idade = st.number_input('Qual a sua idade?', 18, 100)

    tempo_carreira = ['De 0 a 6 meses', 'De 6 meses a 1 ano', 'De 1 ano a 2 anos', 'de 2 anos a 4 anos', 'Mais de 4 anos', 'Não atuo']
    tempo = st.selectbox('Tempo que atua na área de dados', options=tempo_carreira)

with col2:
    livros  = st.radio('Curte Livros?', ['Sim', 'Não'])
    jogos_tabuleiro  = st.radio('Curte Jogos de Tabuleiro?', ['Sim', 'Não'])
    
    estados = ['AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MT', 'PA', 'PB', 'PE', 'PR', 'RJ', 'RN', 'RS', 'SC', 'SP']
    uf = st.selectbox('Estado que mora atualmente', options=estados)

    senioridade = ['Iniciante', 'Júnior', 'Pleno', 'Sênior', 'Gerência','Coordenação', 'Especialista', 'Diretoria', 'C-Level']
    cadeira = st.selectbox('Posição da cadeira (senioridade)', options=senioridade)

with col3:
    jogos_formula1  = st.radio('Curte Jogos de Fórmula 1?', ['Sim', 'Não'])
    jogos_mma  = st.radio('Curte Jogos de MMA?', ['Sim', 'Não'])

    areas_de_formacao = ['Exatas', 'Biológicas', 'Humanas']
    formacao = st.selectbox('Área de Formação', options=areas_de_formacao)

data = {
    'Curte games?': video_game,
    'Curte futebol?': futebol, 
    'Curte livros?': livros,
    'Curte jogos de tabuleiro?': jogos_tabuleiro, 
    'Curte jogos de fórmula 1?': jogos_formula1,
    'Curte jogos de MMA?': jogos_mma, 
    'Idade': idade, 
    'Estado que mora atualmente': uf,
    'Área de Formação': formacao, 
    'Tempo que atua na área de dados': tempo, 
    'Posição da cadeira (senioridade)': cadeira,
}

df = pd.DataFrame([data]).replace({'Sim': 1, 'Não': 0})


dummy_vars = [
    'Estado que mora atualmente',
    'Área de Formação',
    'Tempo que atua na área de dados',
    'Posição da cadeira (senioridade)',
]

colunas_dummy = ['Estado que mora atualmente_AM', 
       'Estado que mora atualmente_BA',
       'Estado que mora atualmente_CE', 'Estado que mora atualmente_DF',
       'Estado que mora atualmente_ES', 'Estado que mora atualmente_GO',
       'Estado que mora atualmente_MA', 'Estado que mora atualmente_MG',
       'Estado que mora atualmente_MT', 'Estado que mora atualmente_PA',
       'Estado que mora atualmente_PB', 'Estado que mora atualmente_PE',
       'Estado que mora atualmente_PR', 'Estado que mora atualmente_RJ',
       'Estado que mora atualmente_RN', 'Estado que mora atualmente_RS',
       'Estado que mora atualmente_SC', 'Estado que mora atualmente_SP',
       'Área de Formação_Biológicas', 'Área de Formação_Exatas',
       'Área de Formação_Humanas',
       'Tempo que atua na área de dados_De 0 a 6 meses',
       'Tempo que atua na área de dados_De 1 ano a 2 anos',
       'Tempo que atua na área de dados_De 6 meses a 1 ano',
       'Tempo que atua na área de dados_Mais de 4 anos',
       'Tempo que atua na área de dados_Não atuo',
       'Tempo que atua na área de dados_de 2 anos a 4 anos',
       'Posição da cadeira (senioridade)_C-Level',
       'Posição da cadeira (senioridade)_Coordenação',
       'Posição da cadeira (senioridade)_Diretoria',
       'Posição da cadeira (senioridade)_Especialista',
       'Posição da cadeira (senioridade)_Gerência',
       'Posição da cadeira (senioridade)_Iniciante',
       'Posição da cadeira (senioridade)_Júnior',
       'Posição da cadeira (senioridade)_Pleno',
       'Posição da cadeira (senioridade)_Sênior', 'Curte games?',
       'Curte futebol?', 'Curte livros?', 'Curte jogos de tabuleiro?',
       'Curte jogos de fórmula 1?', 'Curte jogos de MMA?', 'Idade']

num_vars = [
    'Curte games?',
    'Curte futebol?', 
    'Curte livros?', 
    'Curte jogos de tabuleiro?',
    'Curte jogos de fórmula 1?',
    'Curte jogos de MMA?', 
    'Idade'
]

df_dummy = pd.get_dummies(df[dummy_vars]).astype(int)
df_dummy[num_vars] = df[num_vars]
df = df_dummy

df_template = pd.DataFrame(columns=['Estado que mora atualmente_AM', 
       'Estado que mora atualmente_BA',
       'Estado que mora atualmente_CE', 'Estado que mora atualmente_DF',
       'Estado que mora atualmente_ES', 'Estado que mora atualmente_GO',
       'Estado que mora atualmente_MA', 'Estado que mora atualmente_MG',
       'Estado que mora atualmente_MT', 'Estado que mora atualmente_PA',
       'Estado que mora atualmente_PB', 'Estado que mora atualmente_PE',
       'Estado que mora atualmente_PR', 'Estado que mora atualmente_RJ',
       'Estado que mora atualmente_RN', 'Estado que mora atualmente_RS',
       'Estado que mora atualmente_SC', 'Estado que mora atualmente_SP',
       'Área de Formação_Biológicas', 'Área de Formação_Exatas',
       'Área de Formação_Humanas',
       'Tempo que atua na área de dados_De 0 a 6 meses',
       'Tempo que atua na área de dados_De 1 ano a 2 anos',
       'Tempo que atua na área de dados_De 6 meses a 1 ano',
       'Tempo que atua na área de dados_Mais de 4 anos',
       'Tempo que atua na área de dados_Não atuo',
       'Tempo que atua na área de dados_de 2 anos a 4 anos',
       'Posição da cadeira (senioridade)_C-Level',
       'Posição da cadeira (senioridade)_Coordenação',
       'Posição da cadeira (senioridade)_Diretoria',
       'Posição da cadeira (senioridade)_Especialista',
       'Posição da cadeira (senioridade)_Gerência',
       'Posição da cadeira (senioridade)_Iniciante',
       'Posição da cadeira (senioridade)_Júnior',
       'Posição da cadeira (senioridade)_Pleno',
       'Posição da cadeira (senioridade)_Sênior', 'Curte games?',
       'Curte futebol?', 'Curte livros?', 'Curte jogos de tabuleiro?',
       'Curte jogos de fórmula 1?', 'Curte jogos de MMA?', 'Idade'])

df = pd.concat([df_template, df]).fillna(0)

proba = float(model['model'].predict_proba(df[colunas_dummy])[:,1][0])

if proba > 0.7:
    st.success(f'#### Voce é uma pessoa feliz! Probabilidade: {100 * proba:.0f}%')

elif proba > 0.5:
    st.warning(f'#### Voce é uma pessoa meio feliz! Probabilidade: {100 * proba:.0f}%')

else:
    st.error(f'#### Voce é uma pessoa nada feliz! Probabilidade: {100 * proba:.0f}%')