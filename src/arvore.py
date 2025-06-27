# %% 

import pandas as pd
from sklearn import linear_model, tree

# %%

df = pd.read_csv('../data/processed/dados_processados.csv')
df.head()

# %%

features = df.columns[:-1].to_list()

X = df[features] # features
y = df['Pessoa feliz'] # target

# %%

arvore = tree.DecisionTreeClassifier(random_state=42)

arvore.fit(X, y)

# %%

pd.Series({'model': arvore, 'features': features}).to_pickle('../models/model_feliz.pkl')

# %%
