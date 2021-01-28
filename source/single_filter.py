#This file is for testing single-feature extraction.
import json
import os
import pandas as pd
from glob import glob
#Reading all the files that match a given extension from a directory recursively.
PATH = './reports/report.json'
#PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
#PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
#result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]

with open(PATH) as f:
		data  = json.load(f)
		
df_dataset = pd.DataFrame()
behavior_processes = data['behavior']['processes']
for item in behavior_processes:
	print('PID ' + str(item['pid']) + 'TYPE' + str(type(item['pid'])))
	print('Process Name: ' + str(item['process_name']) + 'TYPE' + str(type(item['process_name'])))
	print('PPID: ' + str(item['ppid']) + 'TYPE' + str(type(item['ppid'])))

"""
print(result[0])
if 'Goodware' in result[0]:
	print(result[0].split('Analisis/')[1][0])
if 'Ransomware' in result[300]:
	print(result[300].split('Ransomware/')[1][0])
if 'Ransomware' in result[300]:
	print(result[500].split('Ransomware/')[1][0])

print(result[0].split('/Experimento')[0].split('/')[-1])
print(result[300].split('/Experimento')[0].split('/')[-1])
print(result[500].split('/Experimento')[0].split('/')[-1])
"""