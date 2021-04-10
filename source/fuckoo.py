import json
import csv
import os
import sys
import pandas as pd
from functools import reduce
from glob import glob

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

def behavior_processes(features, dataframe, data):
    available = ['pid','process_name','ppid'] 
    if not 'behavior' in data:
        empty_category(available,dataframe)
        return
    else:
        if not 'processes' in data['behavior']:
            empty_category(available,dataframe)
            return
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
def filter(path, dataset_name):
    separator = "/" if os.name=="posix" else "\\"
    PATH = path
    result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]
    dataframes = list()
    features = ['procmemory', 'file', 'urls', 'proc_pid', 
    'network', 'udp', 'tcp', 'hosts', 'dns', 'request', 'domains', 
    'behavior', 
    'processes', 'pid', 'process_name', 'ppid', 
    'summary', 'file_created', 'dll_loaded', 'regkey_opened', 'command_line', 'regkey_read', 'regkey_written']
    for report in result:
        with open(report) as f:
            data  = json.load(f)
        print("Processing: " + str(report))
        global df_dataset
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
        dataframes.append(df_dataset)
    general  = pd.concat(dataframes)
    result_path = '.'+separator+str(dataset_name)+'.csv'
    general.to_csv(result_path, index=False)
    print('Dataset created in '+result_path)

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if isinstance(sys.argv[1],str) and isinstance(sys.argv[2],str):
            if os.path.exists(sys.argv[1]):
                if(os.path.isdir(sys.argv[1])):
                    filter(sys.argv[1], sys.argv[2])
                else:
                    print(str(sys.argv[1])+' is not a directory, make sure to use quotation marks around the directory string.')
            else:
                print('The directory "'+str(sys.argv[1])+'" does not exist, make sure to use quotation marks around the directory string.')
        else:
            print('Enter a valid string!')
    else:
        print('Usage: python3 fuckoo.py "/my/directory/with/json/files" "name_of_dataset"')
