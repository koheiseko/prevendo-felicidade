# %% 

import pandas as pd
from sklearn import linear_model

# %%

df = pd.read_csv('../data/processed/dados_processados.csv')
df.head()

# %%

features = df.columns[:-1].to_list()

X = df[features] # features
y = df['Pessoa feliz'] # target

# %%

regressao_logistica = linear_model.LogisticRegression()

regressao_logistica.fit(X, y)

# %%

pd.Series({'model': regressao_logistica, 'features': features}).to_pickle('../models/model_feliz.pkl')

# %%
