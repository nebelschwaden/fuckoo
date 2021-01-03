import json
import csv
import os
import pandas as pd
from functools import reduce
from glob import glob

#Dataframe per report
df_dataset = pd.DataFrame()

#Translates a list of any primitive datatype to a column in the main dataframe
def list_tofeature(values, name, dataframe):
	global df_dataset
	df_dataset = pd.concat([df_dataset,pd.DataFrame(pd.Series(values),columns=[name])],axis=1)
	#dataframe[name] = pd.Series(values)

#Translates all of the column of a certain dataframe into columns in the main dataframe
def dict_tofeatures(dict_list, dataframe):
	dataframe = pd.concat([dataframe,pd.DataFrame(dict_list)], axis=1)
	return dataframe

def empty_category(list,dataframe):
	for x in list:
		list_tofeature([],x,dataframe)
#Reading all the files that match a given extension from a directory recursively.
#PATH = './reports/'
PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]

#Main dataframe
dataframes = list()

#Selected features
features = ['procmemory', 'file', 'urls', 'proc_pid', 
'network', 'udp', 'tcp', 'hosts', 'dns', 'request', 'domains', 
'behavior', 
'processes', 'pid', 'process_name', 'ppid', 
'summary', 'file_created', 'dll_loaded', 'regkey_opened', 'command_line', 'regkey_read', 'regkey_written']

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
				if x == 'urls': #In this case, this is an array of arrays.
					list_tofeature(reduce(lambda x,y: x+y,procmemory_feature),x,dataframe)
				else:
					list_tofeature(procmemory_feature,x,dataframe)
			elif x=='proc_pid': #Repeated 'pid' in behaviour
				if 'pid' in category[0]:
					for item in category:
						procmemory_feature.append(item['pid'])
					list_tofeature(procmemory_feature,'proc_pid',dataframe)
				else:
					list_tofeature([],'proc_pid',dataframe)	
			else:
				list_tofeature([],x,dataframe)

def behavior_processes(features, dataframe, data):
	available = ['pid','process_name','ppid'] #Repeated 'pid' in procmemory -> Solved!
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
	available = ['udp', 'tcp', 'hosts', 'request', 'domains'] # 'dns' feature deleted
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
	with open(report) as f:
		data  = json.load(f)
	print("Processing: " + str(report))
	df_dataset = pd.DataFrame() #A new dataframe is created every time we process a new file.
								#We can take advantage of this ot put the artifact ID and environment per dataframe.

	#procmemory
	procmemory(features,df_dataset,data)

	#network
	#They have their own set of features.
	########################################DISCLAIMER######################################
	######################An ID is given to every set of sub_features#######################
	#The 'concat' function returns a new dataframe.
	network(features,df_dataset,data)
	""" IF NEEDED """
	"""
	category = data['network']
	if 'udp' in features:
		if 'udp' in category:
			df_dataset = dict_tofeatures(category['udp'],df_dataset) #If needed
		else:
			sub_network = ['src','dst','offset','time','dport','sport']
			for y in sub_network:
				list_tofeature([],y,df_dataset)

	if 'tcp' in features:
		if 'tcp' in category:
			df_dataset = dict_tofeatures(category['tcp'],df_dataset)
		else:
			sub_network = ['src','dst','offset','time','dport','sport']
			for y in sub_network:
				list_tofeature([],y,df_dataset)

	if 'hosts' in features:	
		list_tofeature(data['network']['hosts'],'hosts',df_dataset)
	if 'request' in features:
		network_dns_requests = []
		for item in data['network']['dns']:
			network_dns_requests.append(item['request'])
		list_tofeature(network_dns_requests,'requests',df_dataset)
	if 'domains' in features:
		df_dataset = dict_tofeatures(data['network']['domains'],df_dataset)
	"""

	#behavior
	#behavior_processes
	behavior_processes(features,df_dataset,data)
	
	#behavior_summary
	behavior_summary(features,df_dataset,data)
	
	df_dataset.fillna('N/A',inplace=True)
	dataframes.append(df_dataset)


result  = pd.concat(dataframes)
result.to_csv('./raw/raw.csv')





##########################################Save to CSV################################################
#network
"""
dict_list_tocsv('./raw/network/udp/udp_raw.csv',data['network']['udp']) #udp
dict_list_tocsv('./raw/network/tcp/tcp_raw.csv',data['network']['tcp']) #tcp
list_tocsv('./raw/network/hosts/hosts_raw.csv', data['network']['hosts'], 'hosts') #hosts
dict_list_tocsv('./raw/network/dns/dns_raw.csv',data['network']['dns']) #dns -> There is an array of dicts inside, it is being saved in a single cell
requests = [item['request'] for item in data['network']['dns']] #We can use 'if' inside a comprehension list
list_tocsv('./raw/network/dns/requests_raw.csv', requests, 'request') #request
dict_list_tocsv('./raw/network/domains/domains_raw.csv',data['network']['domains']) #domains
"""

#procmemory
"""
procmemory_file, procmemory_urls, procmemory_pid = ([] for i in range(3))
for item in data['procmemory']:
	procmemory_file.append(item['file']) #One String
	procmemory_urls.append(item['urls']) #Array of Arrays of Strings
	procmemory_pid.append(item['pid']) #Integer 
list_tocsv('./raw/procmemory/file/file_raw.csv',procmemory_file,'file')
list_tocsv('./raw/procmemory/urls/urls_raw.csv',reduce(lambda x,y: x+y,procmemory_urls),'urls')
"""

#behavior_processes
"""
behavior_processes = data['behavior']['processes'] #Array of Objects
behavior_processes_pid,behavior_processes_processname,behavior_processes_ppid = ([] for i in range(3))
for item in behavior_processes:
	behavior_processes_pid.append(item['pid']) #Array of Integers
	behavior_processes_processname.append(item['process_name']) #Array of Strings
	behavior_processes_ppid.append(item['ppid']) #Array of Integers
list_tocsv('./raw/behavior/processes/pid/pid_raw.csv', behavior_processes_pid, 'pid') #pids
list_tocsv('./raw/behavior/processes/process_name/processname_raw.csv', behavior_processes_processname, 'process_name') #names of processes
list_tocsv('./raw/behavior/processes/ppid/ppid_raw.csv', behavior_processes_ppid, 'ppid') #ppids
"""

#behavior_summary
"""
behavior_summary_filecreated = data['behavior']['summary']['file_created'] #List of strings (files created)
list_tocsv('./raw/behavior/summary/file_created/filecreated_raw.csv',behavior_summary_filecreated,'file_created')
behavior_summary_dllloaded = data['behavior']['summary']['dll_loaded'] #List of strings (dll's loaded)
list_tocsv('./raw/behavior/summary/dll_loaded/dllloaded_raw.csv',behavior_summary_dllloaded,'dll_loaded')
behavior_summary_regkeyopened = data['behavior']['summary']['regkey_opened'] #List of strings
list_tocsv('./raw/behavior/summary/regkey_opened/regkeyopened_raw.csv',behavior_summary_regkeyopened,'regkey_opened')
behavior_summary_commandline = data['behavior']['summary']['command_line'] #List of strings
list_tocsv('./raw/behavior/summary/command_line/commandline_raw.csv',behavior_summary_commandline,'command_line')
behavior_summary_regkeyread = data['behavior']['summary']['regkey_read'] #List of strings
list_tocsv('./raw/behavior/summary/regkey_read/regkeyread_raw.csv',behavior_summary_regkeyread,'regkey_read')
behavior_summary_regkeywritten = data['behavior']['summary']['regkey_written'] #List of strings
list_tocsv('./raw/behavior/summary/regkey_written/regkeywritten_raw.csv',behavior_summary_regkeywritten,'regkey_written')
"""

##########################################Obtain data################################################
#procmemory
"""
procmemory_file, procmemory_urls, procmemory_pid = ([] for i in range(3))
for item in data['procmemory']:
	procmemory_file.append(item['file']) #One String
	procmemory_urls.append(item['urls']) #Array of Arrays of Strings
	procmemory_pid.append(item['pid']) #Integer
"""

#network
"""
network_udp = data['network']['udp'] #Array of dictionaries
network_tcp = data['network']['tcp'] #Array of dictionaries
network_hosts = data['network']['hosts'] #Array of Strings
network_dns = data['network']['dns'] #Array of dictionaries
network_dns_requests = [] #Array of Strings
for item in network_dns:
	network_dns_requests.append(item['request'])
network_domains = data['network']['domains'] #Array of dictionaries
"""

#behavior_processes
"""
behavior_processes = data['behavior']['processes']
behavior_processes_pid,behavior_processes_processname,behavior_processes_ppid = ([] for i in range(3))
for item in behavior_processes:
	behavior_processes_pid.append(item['pid']) #Array of Integers
	behavior_processes_processname.append(item['process_name']) #Array of Strings
	behavior_processes_ppid.append(item['ppid']) #Array of Integers
"""


#behavior_summary
"""
behavior_summary_filecreated = data['behavior']['summary']['file_created'] #List of strings (files created)
behavior_summary_dllloaded = data['behavior']['summary']['dll_loaded'] #List of strings (dll's loaded)
behavior_summary_regkeyopened = data['behavior']['summary']['regkey_opened'] #List of strings
behavior_summary_commandline = data['behavior']['summary']['command_line'] #List of strings
behavior_summary_regkeyread = data['behavior']['summary']['regkey_read'] #List of strings
behavior_summary_regkeywritten = data['behavior']['summary']['regkey_written'] #List of strings
"""
######################################Check if data is present in the file###################################
#if 'title' in data['glossary']:
#	print("True")
#else:
#	print("False")

#TODO
#When using the UI to select the features to be used, we can check all the features and just allow those that are in the report.json file to be selected.
	#This is only possible if the program processes one file at a time (e.g. it chooses the file to be processed)
	#If we want the program to process dozens of files at the same time, we will not be able to implement this restriction.
#Check with a conditional statement if the used directories exist. Otherwise, a runtime error will appear.
#Delete the useless 'dataframe' parameter for all functions.

