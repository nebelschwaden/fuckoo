import json
import csv
import os
import pandas as pd
from functools import reduce
from glob import glob
##############################DELETE THIS###################

import time
import random
from random import shuffle
start = time.time()

#res = random.sample(range(520), 40)
#counter = 0

############################################################

df_dataset = pd.DataFrame()

def list_tofeature(values, name, dataframe):
    global df_dataset
    df_dataset = pd.concat([df_dataset,pd.DataFrame(pd.Series(values),columns=[name])],axis=1)

def dict_tofeatures(dict_list, dataframe):
    dataframe = pd.concat([dataframe,pd.DataFrame(dict_list)], axis=1)
    return dataframe

def empty_category(list,dataframe):
    for x in list:
        list_tofeature([],x,dataframe)

#PATH = './reports/'
#PATH = './home/nebelschwaden/Documents/Proyecto/Repository/reports/'
PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Old/Analisis/'
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]
###DELETE###
#shuffle(result)
############
dataframes = list()

features = ['procmemory', 'file', 'urls', 'proc_pid', 
'network', 'udp', 'tcp', 'hosts', 'dns', 'request', 'domains', 
'behavior', 
'processes', 'pid', 'process_name', 'ppid', 
'summary', 'file_created', 'dll_loaded', 'regkey_opened', 'command_line', 'regkey_read', 'regkey_written']
"""
features = ['procmemory', 'file', 'proc_pid', 
'network', 'tcp', 'hosts', 'dns', 'domains', 
'behavior', 
'processes', 'pid', 'process_name', 'ppid',
'summary', 'file_created', 'dll_loaded', 'command_line']
"""
def procmemory(features, dataframe, data):
    available = ['file','urls','proc_pid']
    if not 'procmemory' in data:
        empty_category(available,dataframe)
        return
    for x in available:
        if x in features:
            procmemory_feature = []
            category = data['procmemory']
            if x in category[0]:
                for item in category:
                    procmemory_feature.append(item[x])
                if x == 'urls': 
                    list_tofeature(reduce(lambda x,y: x+y,procmemory_feature),x,dataframe)
                else:
                    list_tofeature(procmemory_feature,x,dataframe)
            elif x=='proc_pid': 
                if 'pid' in category[0]:
                    for item in category:
                        procmemory_feature.append(item['pid'])
                    list_tofeature(procmemory_feature,'proc_pid',dataframe)
                else:
                    list_tofeature([],'proc_pid',dataframe)	
            else:
                list_tofeature([],x,dataframe)

#If this function is called, at least one child has been selected
def behavior_processes(features, dataframe, data):
    available = ['pid','process_name','ppid'] 
    if not 'behavior' in data:
        empty_category(available,dataframe)
        return
    else:
        if not 'processes' in data['behavior']:
            empty_category(available,dataframe)
            return
    #The flow in this function is different because we have to group each process features.
    category = data['behavior']['processes']
    beh_process_groups = []
    selected = []
    for x in available:
        if x in features:
            selected.append(x)
    for item in category:
        beh_process_group = {}
        for esc in selected:
            if esc in item:
                    beh_process_group[esc] = item[esc]
            else:
                    beh_process_group[esc] = ''
        beh_process_groups.append(beh_process_group)
    list_tofeature(beh_process_groups,'proc',dataframe)

def behavior_summary(features, dataframe, data):
    available = ['file_created','dll_loaded','regkey_opened','command_line','regkey_read','regkey_written']
    if not 'behavior' in data:
        empty_category(available,dataframe)
        return
    else:
        if not 'summary' in data['behavior']:
            empty_category(available,dataframe)
            return
    for x in available:
        if x in features:
            category = data['behavior']['summary']
            if x in category:
                list_tofeature(category[x],x,dataframe)
            else:
                list_tofeature([],x,dataframe)

def network(features, dataframe, data):
    available = ['udp', 'tcp', 'hosts', 'request', 'domains'] 
    if not 'network' in data:
        empty_category(available,dataframe)
        return
    for x in available:
        if x in features:
            category = data['network']
            if x in category:
                list_tofeature(category[x],x,dataframe)
            elif x=='request':
                if 'dns' in category:
                    network_dns_requests = []
                    for item in data['network']['dns']:
                        network_dns_requests.append(item['request'])
                    list_tofeature(network_dns_requests,'requests',df_dataset)
                else:
                    list_tofeature([],x,dataframe)	
            else:
                list_tofeature([],x,dataframe)


for report in result:
    ##############DELETE THIS#############
    """"
    if not counter in res:
        counter += 1
        continue
    counter += 1
    """
    ######################################
    with open(report) as f:
        data  = json.load(f)
    print("Processing: " + str(report))
    df_dataset = pd.DataFrame()
    if 'procmemory' in features:
        procmemory(features,df_dataset,data)
    if 'network' in features:
        network(features,df_dataset,data)
    if 'behavior' in features:
        if 'processes' in features:
            behavior_processes(features,df_dataset,data)
        if 'summary' in features:
            behavior_summary(features,df_dataset,data)
    df_dataset.fillna('N/A',inplace=True)
    df_dataset.insert(0,'family','')
    if 'Goodware' in report:
        df_dataset['family'] = report.split('Analisis/')[1][0]
    else:
        df_dataset['family'] = report.split('Ransomware/')[1][0]
    df_dataset.insert(0,'artifact','')
    df_dataset['artifact'] = report.split('/Experimento')[0].split('/')[-1]
    dataframes.append(df_dataset)

general  = pd.concat(dataframes)
#TODO sort final by artifact
result_path = './raw/duplicates.csv'
general.to_csv(result_path, index=False)
end = time.time()
print('Runtime:'+str(end - start))
print('Number of rows:'+str(len(general)))
#WE NEED TO ASSIGN IDS WITH THE WHOLE DATAFRAME, OTHERWISE WE WILL END UP WITH REPEATED IDS IN COLUMNS
#The same feature data (proc,ulr,reg_key,etc.) for two different artifacts are given two different ID's
#This allow us to delete duplicates based on the ID -> the ID is linked to the artifact
    # No -> Deleting duplicates will result in less rows, we need to do it per artifact subdataframe
        #Perhaps if we asign ids and then delete duplicates per subdataframe
#A + X -> 1
#A + X -> 1 -> Duplicate
#B + X -> 2 
#B + X -> 2

#TODO Delete duplicates
#Load csv into dataframe
#Get unique values from the 'artifact'  column
#Get sub_dataframe by 'artifact'
#Delete repeated entries for each column for each sub_dataframe
#Should ignore the 'N/A' values -> Secuenciamos todos los valores por columna y los ponemos, lo que resta de espacio se llena con N/A

#Not load, work directly with the 'general' dataframe
#New general dataframe
#Get unique 'artifact' name from 'general' dataframe
#For each unique name, new subdataframe
#For each subdataframe column, drop duplicates
#Append each column to a new artiframe
#Fillna to finished artiframe
#Append artiframe to a list of dataframes
#pd.concat to the list of dataframes
    #Here we can assign id's as well (based on 'artifact' and column) 
    #because there may be the same data in two different artifacts
    #but for troubleshooting, we'll do it at the end
#write to csv
#after checking that the whole dataset does not have mixed columns, we can start by assigning id's

dataframes_clean = list()
artifacts = general['artifact'].unique().tolist()
for item in artifacts:
    subdataframe = general.loc[general['artifact'] == item] #Get dataframe per artifact
    artiframe = pd.DataFrame()
    for col in subdataframe.columns:
        if col != 'artifact' and col != 'family':
            column = subdataframe[col].drop_duplicates()
            artiframe = pd.concat([artiframe,pd.DataFrame(pd.Series(column),columns=[col])],axis=1)
    artiframe.insert(0,'family','') #Perhaps there is a better way to do this...
    artiframe['family'] = subdataframe['family'][0]
    artiframe.insert(0,'artifact','')
    artiframe['artifact'] = item
    artiframe.fillna('N/A',inplace=True)
    dataframes_clean.append(artiframe)
general_final = pd.concat(dataframes_clean)
general_final.to_csv('./raw/general_clean.csv', index=False)
#To view this results, compare the general_clean.csv last lines artifact (Locky) with the same rows in the log_40.csv file