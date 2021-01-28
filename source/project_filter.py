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
PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
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

def behavior_processes(features, dataframe, data):
	available = ['pid','process_name','ppid'] 
	if not 'behavior' in data:
		empty_category(available,dataframe)
		return
	else:
		if not 'processes' in data['behavior']:
			empty_category(available,dataframe)
			return
	for x in available:
		if x in features:
			beh_process_feature = []
			category = data['behavior']['processes']
			if x in category[0]:
				for item in category:
					beh_process_feature.append(item[x])
				list_tofeature(beh_process_feature,x,dataframe)
			else:
				list_tofeature([],x,dataframe)

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
	procmemory(features,df_dataset,data)
	network(features,df_dataset,data)
	behavior_processes(features,df_dataset,data)
	behavior_summary(features,df_dataset,data)
	df_dataset.fillna('N/A',inplace=True)
	if 'Goodware' in report:
		df_dataset.insert(0,'family','')
		df_dataset['family'] = report.split('Analisis/')[1][0]
	else:
		df_dataset.insert(0,'family','')
		df_dataset['family'] = report.split('Ransomware/')[1][0]
	df_dataset.insert(0,'artifact','')
	df_dataset['artifact'] = report.split('/Experimento')[0].split('/')[-1]
	dataframes.append(df_dataset)

final  = pd.concat(dataframes)
#TODO sort final by artifact
result_path = './raw/duplicates.csv'
final.to_csv(result_path, index=False)
end = time.time()
print('Runtime:'+str(end - start))
print('Number of rows:'+str(len(final)))

#TODO Delete duplicates
#Load csv into dataframe
#Get unique values from the artifact name column
#Get sub_dataframe by artifact
#Delete repeated entries for each column for each sub_dataframe
#Should ignore the 'N/A' values -> Secuenciamos todos los valores por columna y los ponemos, lo que resta de espacio se llena con N/A