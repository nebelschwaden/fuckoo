import pandas as pd
dataframe = pd.read_csv('./raw/raw.csv')
head = []
df_dataset = pd.DataFrame()
for col in dataframe.columns: 
    head.append(col)
for i in range(1,len(head)):
    df_dataset[head[i]] = dataframe.groupby([head[i]]).ngroup() #head[0] is the index column of the DF

df_dataset.to_csv('./raw/ids.csv')
