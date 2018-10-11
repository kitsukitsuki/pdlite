import pandas as pd

df = pd.DataFrame()
df = pd.DataFrame.from_csv('tmp.csv')
df.at[1, 'rew']
df_2 = pd.DataFrame.from_csv('tmp.csv')
df.append(df_2)