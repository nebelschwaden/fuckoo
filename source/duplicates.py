import pandas as pd
general = pd.read_csv('./raw/logs/log_40.csv')
dataframes_clean = list()
artifacts = general['artifact'].unique().tolist()
for item in artifacts:
    subdataframe = general.loc[general['artifact'] == item] #Get dataframe per artifact
    artiframe = pd.DataFrame()
    for col in subdataframe.columns:
        if col != 'artifact' and col != 'family':
            column = subdataframe[col].drop_duplicates()
            artiframe = pd.concat([artiframe,pd.DataFrame(pd.Series(column),columns=[col])],axis=1)
    artiframe.insert(0,'family','')
    artiframe['family'] = subdataframe.iloc[0]['family']
    artiframe.insert(0,'artifact','')
    artiframe['artifact'] = item
    artiframe.fillna('N/A',inplace=True)
    dataframes_clean.append(artiframe)
general_final = pd.concat(dataframes_clean)
general_final.to_csv('./raw/general_clean.csv', index=False)
#To view this results, compare the general_clean.csv last lines artifact (Locky) with the same rows in the log_40.csv file