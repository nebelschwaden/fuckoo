import pandas as pd
dataframe = pd.read_csv('./raw/duplicates.csv')
head = []
df_dataset = pd.DataFrame()
for col in dataframe.columns: 
    head.append(col)
#TODO add to 'group by' the 'artifact name' column

for i in range(1,len(head)): 
    df_dataset[head[i]] = dataframe.groupby([head[i]]).ngroup() #head[0] is the index column of the DF


df_dataset.to_csv('./raw/d_ids.csv')
