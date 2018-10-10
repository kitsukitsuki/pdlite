import pandas as pd

df = pd.DataFrame()
df = pd.DataFrame.from_csv('tmp.csv')
df.at[1, 'rew']