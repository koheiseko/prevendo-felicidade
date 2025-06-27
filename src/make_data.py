# %%

import pandas as pd

df = pd.read_csv('../data/raw/dados_comunidade.csv')
df.head()

# %%

df.replace({'Sim': 1, 'Não': 0}, inplace=True)

num_vars = [
    'Curte games?',
    'Curte futebol?', 
    'Curte livros?', 
    'Curte jogos de tabuleiro?',
    'Curte jogos de fórmula 1?',
    'Curte jogos de MMA?', 
    'Idade',
]

dummy_vars = [
    'Estado que mora atualmente',
    'Área de Formação',
    'Tempo que atua na área de dados',
    'Posição da cadeira (senioridade)',
]

df_processed = pd.get_dummies(df[dummy_vars]).astype(int)
df_processed[num_vars] = df[num_vars].copy()

df_processed['Pessoa feliz'] = df['Você se considera uma pessoa feliz?'].copy()

df_processed.head()

df_processed.to_csv('../data/processed/dados_processados.csv', index=False)

