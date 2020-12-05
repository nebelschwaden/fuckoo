import json
import csv
import pandas as pd
from functools import reduce
#We can modify every json file so that it only contains the features that we want.
with open('report.json') as f:
	data  = json.load(f)

#Saves a list of dictionaries to a csv file
def dict_list_tocsv(filepath, dict_list):
	df_dict_list = pd.DataFrame(dict_list) #This does not work properly with nested data
	df_dict_list.to_csv(filepath) #Add the mode='a' flag to append data to an existing csv

#Saves a list of any primitive datatype to a csv file
def list_tocsv(filepath, list, name):
	series_list = pd.Series(list)
	series_list.to_csv(filepath, header=[name])


##########################################Save to CSV################################################
#network
#dict_list_tocsv('./raw/network/udp/udp_raw.csv',data['network']['udp']) #udp
#dict_list_tocsv('./raw/network/tcp/tcp_raw.csv',data['network']['tcp']) #tcp
#list_tocsv('./raw/network/hosts/hosts_raw.csv', data['network']['hosts'], 'hosts') #hosts
#dict_list_tocsv('./raw/network/dns/dns_raw.csv',data['network']['dns']) #dns -> There is an array of dicts inside, it is being saved in a single cell
#requests = [item['request'] for item in data['network']['dns']] #We can use 'if' inside a comprehension list
#list_tocsv('./raw/network/dns/requests_raw.csv', requests, 'request') #request
#dict_list_tocsv('./raw/network/domains/domains_raw.csv',data['network']['domains']) #domains

#procmemory
procmemory_file, procmemory_urls, procmemory_pid = ([] for i in range(3))
for item in data['procmemory']:
	#procmemory_file.append(item['file']) #One String
	#procmemory_urls.append(item['urls']) #Array of Arrays of Strings
	procmemory_pid.append(item['pid']) #Integer 
#list_tocsv('./raw/procmemory/file/file_raw.csv',procmemory_file,'file')
#list_tocsv('./raw/procmemory/urls/urls_raw.csv',reduce(lambda x,y: x+y,procmemory_urls),'urls')







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
########################################Check if data is in the file######################################
#if 'title' in data['glossary']:
#	print("True")
#else:
#	print("False")

#TODO
#Check with a conditional statement if the used directories exist. Otherwise, a runtime error will appear.
#Check if the wanted data exists in the report.json file