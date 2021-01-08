import json
import os
import pandas as pd
from glob import glob
#Reading all the files that match a given extension from a directory recursively.
PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
#PATH = '/home/nebelschwaden/Documents/Proyecto/Data/Analisis/'
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.json'))]
"""
with open(result[0]) as f:
		data  = json.load(f)
		
df_dataset = pd.DataFrame()
network_tcp = data['network']['tcp']
print(network_tcp)
print(len(network_tcp))
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