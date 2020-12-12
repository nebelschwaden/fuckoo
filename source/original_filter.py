import json
import csv
import pandas as pd
from functools import reduce
#We can modify every json file so that it only contains the features that we want.
with open('./reports/report.json') as f:
	data  = json.load(f)
df_dataset = pd.DataFrame() #Main dataframe
#Saves a list of dictionaries to a csv file
def dict_list_tocsv(filepath, dict_list):
	df_dict_list = pd.DataFrame(dict_list) #This does not work properly with nested data
	df_dict_list.to_csv(filepath) #Add the mode='a' flag to append data to an existing csv

#Saves a list of any primitive datatype to a csv file
def list_tocsv(filepath, list, name):
	series_list = pd.Series(list)
	series_list.to_csv(filepath, header=[name])

#Translates a list of any primitive datatype to a column in the main dataframe
def list_tofeature(list, name):
	df_dataset[name] = pd.Series(list)

#Translates all of the column of a certain dataframe into columns in the main dataframe
def dict_tofeatures(dict_list):
	global df_dataset
	df_dataset = pd.concat([df_dataset,pd.DataFrame(dict_list)], axis=1)

######################################General Dataframe##############################################
#procmemory
procmemory_file, procmemory_urls, procmemory_pid = ([] for i in range(3))
for item in data['procmemory']:
	procmemory_file.append(item['file']) #One String
	procmemory_urls.append(item['urls']) #Array of Arrays of Strings
	procmemory_pid.append(item['pid']) #Integer
list_tofeature(procmemory_file,'file')
list_tofeature(reduce(lambda x,y: x+y,procmemory_urls), 'urls')
list_tofeature(procmemory_pid,'pid')

#network
dict_tofeatures(data['network']['udp'])
dict_tofeatures(data['network']['tcp'])
list_tofeature(data['network']['hosts'],'hosts')
network_dns = data['network']['dns']
#dict_tofeatures(network_dns)
network_dns_requests = []
for item in network_dns:
	network_dns_requests.append(item['request'])
list_tofeature(network_dns_requests,'requests')
dict_tofeatures(data['network']['domains'])

#behavior
#behavior_processes
behavior_processes = data['behavior']['processes'] #Array of Objects
behavior_processes_pid,behavior_processes_processname,behavior_processes_ppid = ([] for i in range(3))
for item in behavior_processes:
	behavior_processes_pid.append(item['pid']) #Array of Integers
	behavior_processes_processname.append(item['process_name']) #Array of Strings
	behavior_processes_ppid.append(item['ppid']) #Array of Integers
list_tofeature(behavior_processes_pid,'pid')
list_tofeature(behavior_processes_processname,'process_name')
list_tofeature(behavior_processes_ppid,'ppid')

#behavior_summary
behavior_summary_filecreated = data['behavior']['summary']['file_created'] #List of strings (files created)
list_tofeature(behavior_summary_filecreated,'file_created')
behavior_summary_dllloaded = data['behavior']['summary']['dll_loaded'] #List of strings (dll's loaded)
list_tofeature(behavior_summary_dllloaded,'dll_loaded')
behavior_summary_regkeyopened = data['behavior']['summary']['regkey_opened'] #List of strings
list_tofeature(behavior_summary_regkeyopened,'regkey_opened')
behavior_summary_commandline = data['behavior']['summary']['command_line'] #List of strings
list_tofeature(behavior_summary_commandline,'command_line')
behavior_summary_regkeyread = data['behavior']['summary']['regkey_read'] #List of strings
list_tofeature(behavior_summary_regkeyread,'regkey_read')
behavior_summary_regkeywritten = data['behavior']['summary']['regkey_written'] #List of strings
list_tofeature(behavior_summary_regkeywritten,'regkey_written')

df_dataset.to_csv('./raw/raw_original.csv')



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
#Check if the wanted data exists in the report.json file
#We can concatenate each main dataframe from each report.json file to obtain a final dataframe.